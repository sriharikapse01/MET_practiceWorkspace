# Multiply Dictionary Values if Key Starts with 'a'
# Given dictionary: {'apple': 2, 'banana': 3, 'apricot': 4, 'berry': 5}. 
# Multiply values where keys start with 'a'.
# Expected Output: Product of values: 8

a = {
    'apple': 2,
    'banana': 3, 
    'apricot': 4, 
    'berry': 5
    }
product = 1
for i in a:
    if i.startswith('a'):
       product *= a[i]
print(f"product of values: {product}")