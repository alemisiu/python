print("Welcome to the calculator:")
bill = float(input("What was the total bill $: "))
tip = int(input("what percentage tip would u like to give : 10 , 12 , 15 "))
people = int(input("how many people  to split the bill ?"))
tip_percentage = tip/100
all_payment =bill *tip_percentage
total_bill = bill + all_payment
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)

print(f"Each person should pay {final_amount}") 