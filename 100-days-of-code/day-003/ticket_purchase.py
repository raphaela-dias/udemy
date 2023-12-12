#Checks the data type of the user's input
def validation_type(user_input): 
    while True:
        try:
            user_input_coversion = float(user_input) 
            break
        except ValueError:
            print("Invalid value.")
            user_input = input("Please enter a valid value: ")
    return user_input_coversion

#Ticket cost control variable
ticket = 0

print("Welcome to the rollercoaster!")

#Checks user's height
height = input("Please enter your height in cm: ")
valid_height = validation_type(height)
if valid_height >= 120:
    print("You can ride the rollercoaster!")

    #Checks the user's age
    age = input("Please enter your age: ")
    valid_age = validation_type(age)
    if valid_age <= 12:
        print("Your ticket is $5.")
        ticket += 5
    elif 12 < valid_age <= 18:
        print("Your ticket is $7.")
        ticket += 7
    else:
        print("Your ticket is $12")
        ticket += 12 

    #Checks whether the user would like to have their picture taken or not
    photo = ""
    while photo != "y" and photo != "n":
        photo = input("Would you like a photo of the ride?\nEnter 'y' for yes or 'n' for no.")
        if photo == "y":
            ticket += 3
            break
        elif photo == "n":
            break
        else:
            print("Invalid answer.")
    
    #Prints out the final bill
    print(f"Your final bill is ${ticket}.")
else:
    print("Sorry, you have to grow taller before you can ride.")