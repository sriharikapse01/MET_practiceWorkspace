# 10. Print Key-Value Pairs with Length Conditions
# Given dictionary: {'name': 'Alice', 'city': 'New York', 'hobby': 'coding'},
# Print each key-value. 
# If value length > 5, print in uppercase. Else, in lowercase.
# Expected Output:
# name: alice
# city: NEW YORK
# hobby: CODIN

dictionary = {'name': 'Alice',
              'city': 'New York',
              'hobby': 'coding'}
for key, value in dictionary.items():
    if len(value) > 5:
        print(f"{key}: {value.upper()}")
    else:
        print(f"{key}: {value.lower()}")