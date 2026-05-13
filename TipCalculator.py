print("Welcome to tip calculator")
print("@Author: Gopesh Sharma")
print("@Date: 5/13/2026\n")

bill = float(input("What is the amount of total bill? \n"))
no_of_people = int(input("How many people do you want to split the bill? \n"))
tip_percent = float(input("How much percentage do you want to tip 10 15 20? \n"))

total_bill_with_tip = bill + ((bill * tip_percent)/100)

bill_per_person = total_bill_with_tip / no_of_people
print(f"Each person should pay {bill_per_person:.2f}")
