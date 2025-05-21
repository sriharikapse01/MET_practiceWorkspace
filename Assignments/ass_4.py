# 1. Create a dictionary where keys are (username, password) tuples and values are roles:
users = {("john", "1234"): "admin", 
         ("alice", "abcd"): "editor"
         }
# 2. Ask the user:
Username = input("Enter Your User name : ")
Password = input("Enter your password : ")
# 3. Form a tuple from their input.
user = (Username, Password)
role = users[user]
# 4. Check if the tuple exists in the dictionary using if.
if user in users:
    print(f"WELCOME {role} ")
    
else:
    print("invalid")
