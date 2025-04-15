print("Welcome to Python Pizza Deliveries!")

final_bill = 0
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

if size == 'S':
    final_bill += 15
elif size == 'M':
    final_bill += 20
else:
    final_bill += 25

if pepperoni == 'Y':
    if size == 'S':
        final_bill += 2
    else:
        final_bill += 3

if extra_cheese == 'Y':
    final_bill += 1

print(f"Your final bill is ${final_bill}")
