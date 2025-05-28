# 8. Check if Any Number is a Perfect Square
# Given: [10, 25, 36, 40]. Print the first number that is a perfect square. Stop after finding it.
# Expected Output: 25 is a perfect square.

a = [10 , 25 , 36 , 40]
for i in a:
    if (i ** 0.5).is_integer():
        print(f"{i} is a perfet square.")
        break