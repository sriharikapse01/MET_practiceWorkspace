# 1. Create a set of tags:
tags = {"python", "fastapi", "backend"}
# 2. Ask the user to input a new tag.
new_tag = input("New tag : ")
# 3. Use if to check if it exists in the set.
if new_tag in tags:
# 4. If it does, print: "Tag already exists."
    print("Tag already exists.")
# 5. If not, add it using add() and print the updated set.
else:
    tags.add(new_tag)

print(tags)