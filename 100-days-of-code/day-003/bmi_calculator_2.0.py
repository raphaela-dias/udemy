# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters:"))
# Enter your weight in kilograms e.g., 72
weight = float(input("Enter your weight in kilograms: "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you're underweight.")
elif 18.5 < bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif 25 < bmi < 30:
    print(f"Your bmi is {bmi}, you're slightly overweight.")
elif 30 < bmi < 35:
    print(f"Your bmi is {bmi}, you're obese.")
else:
    print(f"Your bmi is {bmi}, you're clinically obese.")