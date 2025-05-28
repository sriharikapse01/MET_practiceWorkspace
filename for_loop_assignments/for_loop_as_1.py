# 1. Sum Even Numbers in a List
# Given a list of numbers: [1, 4, 7, 10, 13, 16].
# Iterate through the list using a for loop. 
# Sum only the even numbers.
# Print the total sum at the end

a = [1, 4, 7, 10, 13, 16]
sum = 0
for i in a:
    if i % 2 == 0:
        sum += i
print("Sum of even numbers in the list:", sum)
