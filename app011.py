print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("you can ride the rollecercoaster!")
    age = int(input("what is your age?"))
    bill = 0
    if age < 12:
        bill = 5
        print("child pay $5.")
    elif age <= 18:
        bill = 7
        print("tados pay $7")
    elif age <= 22:
        bill = 6
        print("youth pay $6")
    elif age <= 45 and age >= 55:
        bill = 0
        print("masz bilet za darmo")
    else:
        bill = 12
        print("adults pay $12.")
    wants_photo = input("do u want photo take Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"your total payment is{bill} :")

else:
    print("sorry, you have to grow taller before you can ride.")
