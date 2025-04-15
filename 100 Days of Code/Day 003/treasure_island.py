'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

left_right = input("You're at a cross road.\nWhere do you want to go?\nType 'left' or 'right'. ").lower()

if left_right == "right":

    swim_wait = input("You've come to a lake.\nThere is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across. ").lower()

    if swim_wait == 'wait':

        door = input("You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue.\nWhich color do you choose? ").lower()

        if door == 'red':
            print("You've entered a room full of fire.\nGame over.")
        elif door == 'blue':
            print("You've entered a room full of monsters.\nGame over.")
        elif door == 'yellow':
            print("You've found the treasure!\nYou win!")
        else:
            print("You ended up in limbo.\nGame over.")
    elif swim_wait == 'swim':
        print("You were attacked by piranhas.\nGame over.")
    else:
        print("You ended up in limbo.\nGame over.")
elif left_right == 'left':
    print("You fell into a hole.\nGame over.")
else:
    print("You ended up in limbo.\nGame over.")