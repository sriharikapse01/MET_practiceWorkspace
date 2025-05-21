
# 1. create a list with one product:
cart = [{"id" : 1,
         "name" : "shirt",
         "qty" : 1}]
#2.ask the user to input:
product_id = int(input("Enter the product ID: "))
product_name = input("Enter the product name: ")
#3. create a dictionary from the user input:
product = {
    "id" : product_id,
    "name" : product_name,
    "qty" : 1
}
# 4.use an if statement to check if the id of
# the new product matches the one already in the cart:
if product["id"] == cart[0]["id"]:
    print("Item already in cart.")
# 5. if it exists, print: "Item already in cart."
else:
    cart.append(product)
# 6. if it doesn’t exist, append it to the list and print the updated cart:
    print("Updated cart:", cart)

print("End of program.")
