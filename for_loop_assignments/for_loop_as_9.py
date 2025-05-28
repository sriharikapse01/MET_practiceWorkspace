# 9. Capitalize Names if Short (Using Tuple)
# Given tuple: ('sam', 'john', 'alex', 'bob'). 
# If the name is 3 or fewer letters, print in uppercase.
# Else,capitalize.
# Expected Output: SAM, John, Alex, BOB

name = ('sam', 'john', 'alex', 'bob')
for n in name:
    if len(n) <= 3:
        print(n.upper(), end = ", ")
    else:
        print(n.capitalize(), end = ", ")
        

