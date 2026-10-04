print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
cross_road = input("Type 'left' or 'right'\n")
if cross_road == "Left" or cross_road ==  "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if lake == "Wait" or lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doors = input("One red, one yellow and one blue. Which colour do you choose?\n")
        if doors == "Red" or doors == "red":
            print("It's a room full of fire. Game Over.")
        elif doors == "Yellow" or doors == "yellow":
            print("You found the treasure! You Win!")
        elif doors == "Blue" or doors == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Incorrect Answer , Game Over!")
    elif lake == "Swim" or lake == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Incorrect Answer , Game Over!")
elif cross_road == "Right" or cross_road =="right":
    print("You fell into a hole. Game Over.")
else:
    print("incorrect Answer, Game Over!")