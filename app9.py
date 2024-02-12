print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("you can ride the rollecercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print ("please pay $5.")
    elif  age <= 18:
        print("please pay $7")
    elif age <= 22:
        print("please pay $6")
    else:
        print("please pay $12.")
else:
    print("sorry, you have to grow taller before you can ride.")
