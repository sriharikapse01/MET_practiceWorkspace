# 1. Create a list:
locations = [(12.9716)]
# 2. Ask the user to input:
Latitude = float(input("Enter Latitude : "))
Longitude = float(input("Enter Longitude : "))
# 3. Combine them into a tuple.
new_location = (Latitude, Longitude)
# 4. Check using if whether this tuple already exists in the list.
if new_location in locations:
# 5. If yes, print: "Location already exists."
    print("Location already exists")
# 6. If no, append the tuple and print the updated list.
else:
    locations.append(new_location)
    
print("updated tuple is " , locations)
    



