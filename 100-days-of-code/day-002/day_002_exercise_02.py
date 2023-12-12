# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

num_height = float(height)
num_weight = float(weight)

result = round(num_weight / num_height ** 2, 2)

print(f"Your BMI is {result}.")