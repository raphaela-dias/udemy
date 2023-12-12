# Which year do you want to check?
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")