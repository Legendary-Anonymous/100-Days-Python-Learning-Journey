rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
random_integer = random.randint(0,2)
computer_choice = random_integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
    print("You Chose:")
    print(rock)
elif user_choice == 1:
    print("You Chose:")
    print(paper)
elif user_choice == 2:
    print("You Chose:")
    print(scissors)


if computer_choice == 0:
    print("Computer Chose:")
    print(rock)
elif computer_choice == 1:
    print("Computer Chose:")
    print(paper)
elif computer_choice == 2:
    print("Computer Chose:")
    print(scissors)

if user_choice == 0 and computer_choice == 0:
    print("It is a tie")
elif user_choice == 0 and computer_choice == 1:
    print("You Lost!")
elif user_choice == 0 and computer_choice == 2:
    print("You Won!")
elif user_choice == 1 and computer_choice == 0:
    print("You Won!")
elif user_choice == 1 and computer_choice == 1:
    print("It is a tie")
elif user_choice == 1 and computer_choice == 2:
    print("You Won!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lost!")
elif  user_choice == 2 and computer_choice == 1:
    print("You Won!")
elif  user_choice == 2 and computer_choice == 2:
    print("It is a tie")
else:
    print("Incorrect selection")
    print("You Lost")