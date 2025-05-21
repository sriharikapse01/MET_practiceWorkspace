# 1. Create a dictionary like
order = {
    "item1": {"name": "Laptop", "price": 700},
    "item2": {"name": "Mouse", "price": 20}
 }
# 2. Ask the user to enter an item key: ("item1" or "item2")
item_key = input("Enter item1 or item2 : ")
# 3. Use an if-elif-else block to:
# • Check which item was entered.
# • Print the item name and price.
if item_key == "item1":
    item = order["item1"]
    print(f"{item['name']},costs ₹{item['price']}")
elif item_key == "item2":
    item = order["item2"]
    print(f"{item['name']},costs ₹{item['price']}")
else:
    print("Item not found")