# 4. Print Squares of Numbers, Skip Multiples of 3
# Given numbers from 1 to 10, print their squares.
# Use continue to skip numbers divisible by 3.
# Expected Output: Squares of all numbers except 3, 6, 9

for i in range(1 , 11):
    if i % 3 == 0:
        continue
    print(i ** 2)
