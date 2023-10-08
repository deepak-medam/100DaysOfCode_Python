print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

##### Simple if else condition #####

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

##### Netsed if-elif-else #####

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay £5")
#     elif age <= 18:
#         print("Please pay £7")
#     else:
#         print("Please pay £12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


#### Multiple conditions ####
# Charge people £3 for a photo. This is independet of age or height.
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child ticket is £5")
        bill += 5
    elif age <= 18:
        print("Youth ticket is £7")
        bill += 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult ticket is £12")
        bill += 12
    
    wants_photo = input("Do you want a photo taken? y or n. ")
    if wants_photo == 'y':
        bill += 3
    print(f"Your final bill is £{bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")