import cv2
import numpy as np

def detect_person_size(image_path, reference_width_cm=21.0):
    image = cv2.imread(image_path)
    if image is None:
        return {"error": "Image not found or unreadable"}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours or len(contours) < 2:
        return {"error": "A4 paper or human not clearly found"}

    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    human_contour = contours[0]
    a4_contour = contours[1]

    # A4 box size
    rect_a4 = cv2.minAreaRect(a4_contour)
    a4_box = cv2.boxPoints(rect_a4)
    a4_box = np.array(a4_box, dtype="int")
    a4_width_pixels = np.linalg.norm(a4_box[0] - a4_box[1])

    if a4_width_pixels == 0:
        return {"error": "A4 reference width is zero"}

    pixels_per_cm = a4_width_pixels / reference_width_cm

    rect_human = cv2.minAreaRect(human_contour)
    human_box = cv2.boxPoints(rect_human)
    human_box = np.array(human_box, dtype="int")

    height_pixels = np.linalg.norm(human_box[0] - human_box[2])
    width_pixels = np.linalg.norm(human_box[1] - human_box[3])

    height_cm = round(height_pixels / pixels_per_cm, 2)
    width_cm = round(width_pixels / pixels_per_cm, 2)

    return {
        "height_cm": height_cm,
        "width_cm": width_cm
    }
