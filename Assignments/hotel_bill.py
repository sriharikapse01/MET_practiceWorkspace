#  You are creating  a hotel bill calculator of Kapse's Hotel.
# they serve dishes like idli, dosa, vada, puri and coffee.
# every customer order three number of dishes.

bill = 0

menu = {
    "idly" : 20,
    "dosa" : 30,
    "vada" : 25,
    "puri" : 15,
    "coffee" : 10
}

item_1 = input("Enter the dish: ")
item_count_1 = int(input("how many items you want: "))

item_2 = input("Enter the dish: ")
item_count_2 = int(input("how many items you want: "))

item_3 = input("Enter the dish: ")
item_count_3 = int(input("how many items you want: "))

bill_1 = menu[item_1] * item_count_1
bill_2 = menu[item_2] * item_count_2
bill_3 = menu[item_3] * item_count_3

bill = (menu[item_1] * item_count_1) + (menu[item_2] * item_count_2) + (menu[item_3] * item_count_3)

print(f"""Your bill is:
      {item_1} X {item_count_1} = {bill_1}
       {item_2} X {item_count_2} = {bill_2}
        {item_3} X {item_count_3} = {bill_3}
        
        TOTAL BILL IS : {bill}
      -----------------KAPSE'S HOTEL-----------------
      -----------------Thank you for visiting-----------------""")