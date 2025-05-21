# Assignment 2: 📂 Product Categories (Dict of Lists)
# 📘 Objective:
#"" Display available products in a given category.""
# Steps:
# 1. Create a dictionary:
# categories = {
#    "clothes": ["shirt", "jeans"],
#    "electronics": ["phone", "charger"]
# }
# Ask the user to input a category name.
# 3. Use an if statement to check if the entered category exists in the dictionary.
# 4. If it exists, print the list of products.
# 5. If not, print "Invalid category."


# 1. Create a dictionary:
categories = {
   "clothes": ["shirt", "jeans"],
   "electronics": ["phone", "charger"]
}

# Ask the user to input a category name.
catagory_name = input("Enter a catagory name: ")
# 3. Use an if statement to check if the entered category exists in the dictionary.
if catagory_name in categories:
    # 4. If it exists, print the list of products.
    print("Products in", catagory_name, "category:", categories[catagory_name])
else:
    # 5. If not, print "Invalid category."
    print("Invalid category.")