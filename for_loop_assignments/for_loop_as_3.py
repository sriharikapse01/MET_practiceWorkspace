# 3. Count Vowels in a String Using a Set
# Given a string: 'Welcome to Python loops',
# count how many vowels (a, e, i, o, u) are in it.
# Use a set to define vowels.
# Expected Output: Vowel count: 7

a = 'Welcome to Python loops'
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0

for i in a:
    if i in vowels:
        count = count + 1
print(f"Vowels count : {count}")