print('''

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
      
''')

print('''Welcome to the treasure island game!
Make your choices to find the treasure... or die trying!\n''')

left_right = input('''You're at a crossroad, where do you want to go?
Type "left" or "right": ''').lower()

if left_right == 'left':

    swim_wait = input('''\nYou've come to a lake.
There is an island in the middle of the lake.
Type "wait" to wait for a boat or "swim" to swim across: ''').lower()
    
    if swim_wait == 'wait':

        door = input('''\nYou've arrived at the island unharmed.
There is a house with 3 doors. One red, one yellow and one blue.
Which color do you choose?
Type 'red', 'yellow' or 'blue': ''').lower()
        
        if door == 'blue':
            print('''\nYou've been attacked by werewolves.
Game over.''')
        elif door == 'yellow':
            print('''\nYou've found the treasure!
Congratulations, you win!''')
        else:
            print('''\nYou've entered a room full of fire.
Game over.''')
            
    else:
        print('''\nYou've been swallowed by the lake Ness monster.
Game over.''')
        
else:
    print('''\nYou fell into a black hole.
Game over.''')