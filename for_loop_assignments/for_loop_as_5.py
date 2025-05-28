# 5. Categorize Numbers using if-elif-else
# Given a list [5, -1, 0, 12, -7],
# print whether each number is Positive, Negative or Zero.
# Expected Output:
# 5 is positive
# -1 is negative
# Zero found
# 12 is positive
# -7 is negative

a = [5 , -1 , 0 , 12 , -7]
for i in a:
    if i > 0:
        print(f"{i} is positive")
    elif i < 0:
        print(f"{i} is negative")
    else:
        print("Zero found")