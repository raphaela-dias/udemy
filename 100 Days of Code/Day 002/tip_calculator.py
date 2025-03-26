print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

percentage = 1 + (tip / 100)
amount_to_pay = round((total_bill * percentage) / number_of_people, 2)

print(f"Each person should pay ${amount_to_pay}")
