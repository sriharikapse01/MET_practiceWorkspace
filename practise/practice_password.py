# password generator and strength checker
# Generate password using string methodas and expressions
# check strength using condiutions
# store password rules in dictionary
# No loop needed - just string manipulation function

# Catagories criteria
weak = 1
fair = 6
good = 8
strong = 12
very_strng = 16

# mandatory criteria
mandatory_criteria = {
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "special_characters": "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"
}

# # eleminate common phrases
# common_phrases = [
#     "password", "123456", "qwerty", "letmein", "iloveyou",
#     "admin", "welcome", "abc123", "trustno1", "monkey"
# ]

password = input("Enter the password : ")
password_length = len(password)
password_strength = " "

if password_length > weak and password_length < fair:
    password_strength = "Weak password"
elif password_length >= fair and password_length < good:
    password_strength = "Fair password"
elif password_length >= good and password_length < strong:
    password_strength = "Good password"
elif password_length >= strong and password_length < very_strng:
    password_strength = "Strong password"
elif password_length >= very_strng:
    password_strength = "Very Strong password"

is_invalid = password.isalnum()
if is_invalid:
    print(f"The password is {password_strength} and invalid")
else:
    print(f"The password is {password_strength} and valid")