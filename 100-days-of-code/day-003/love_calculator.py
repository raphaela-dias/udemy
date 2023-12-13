print("The Love Calculator is calculating your score...")
name1 = input("What is your name?").upper()
name2 = input("What is their name?").upper()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

score_true = 0
score_love = 0
true = ["T", "R", "U", "E"]
love = ["L", "O", "V", "E"]

names = name1 + name2

name_list = list(names)

for letter_name in name_list:
    for letter_true in true:
        if letter_name == letter_true:
            score_true += 1
    
    for letter_love in love:
        if letter_name == letter_love:
            score_love += 1

score = int(str(score_true) + str(score_love))

if 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
elif score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
else:
    print(f"Your score is {score}.")