from backend.db.supabase_client import get_supabase_client


from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from core.detection import detect_person_size
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect/")
async def detect(file: UploadFile = File(...)):
    file_location = "temp.jpg"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    result = detect_person_size(file_location)

    if os.path.exists(file_location):
        os.remove(file_location)

    # Error response
    if "error" in result:
        return result

    # ✅ Use WIDTH to determine clothing size
    width = result["width_cm"]
    if width <= 28:
        size = "S"
    elif 28 <= width <= 34:
        size = "M"
    elif 34 <= width <= 40:
        size = "L"
    else:
        size = "XL"

    # Save to DB
    supabase = get_supabase_client()
    supabase.table("detections").insert({
        "height_cm": result["height_cm"],
        "width_cm": width,
        "size": size
    }).execute()

    # Add size to response
    result["size"] = size
    return result
