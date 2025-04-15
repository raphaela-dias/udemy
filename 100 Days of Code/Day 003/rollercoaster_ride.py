print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    bill = 0
    print("You can ride the rollercoaster!")

    age = int(input("How old are you? "))
    if age < 12:
        print("Child tickets are $5")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill += 7
    else:
        if age >= 45 and age <= 55:
            print("You ride for free")
        else:
            print("Adult tickets are $12")
            bill +=12

    photo = input("Would you like to keep a picture of the ride? Y - Yes or N - no ").upper()

    if photo == 'Y':
        bill += 3

    print(f"Your bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")