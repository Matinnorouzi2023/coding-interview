import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper, scissors]
user_choice = int(input(" what do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n"))


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_image[user_choice])

    computer_choice = random.randint(0,2)
    print("computer_choice ")
    print(game_image[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("I lose!")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("I win!")
    elif computer_choice == user_choice:
        print("It's a draw")
