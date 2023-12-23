#Number Guessing Game Objectives:

# Include an ASCII art logo.

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# function to checlk user's guess against actual answer.
def check_answer(guess, answer, turns):
  """"checks answer against guess. Returns the number of remaining """
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f" You got it! The answer was{answer}.")
# make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficultyy.Type 'easy' or 'hard':")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  # Allow the player to submit a guess for a number between 1 and 100.
  print("Wellcome to the Number Guessing Game")
  print("I'm thinking of a number between 1 and 100.")
  answer =  randint(1,100)
  print(f"guess, the correct answer is {answer}")
  turns = set_difficulty()


  # If they got the answer correct, show the actual answer to the player.

  #Reapeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaing to guess the number.")
    #Let the user guess a number.
    guess = 0
    guess = int(input("Make a guess:"))
    turns = check_answer(guess,answer,turns)
    if turns ==0 :
      print(" You've ran out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
game()


# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).




# level = input("Type 'easy' or 'hard' level:")
# print("choose a diffoculty. Type 'easy' or 'hard':{level}")
#
#
# user_guess = input("Guess a number between 1 and 100")
# print(f"guess a number {user_guess}")
# actual_answer = 15
# if level == "easy":
#   for _ in range(10, 0):
#         print(f"actual_answer is {actual_answer}")
#       if user_guess == actual_answer:
#         print(" you win")
#       elif user_guess > actual_answer:
#         print("Too high")
#         print("Guess again")
#       elif user_guess < actual_answer:
#         print("Too low")
#         print("Guess again")
#       else:
#         print("You've run out of guesses, you lose.")
# else:
#   for _ in range(5, 0):
#       print(f"actual_answer is {actual_answer}")
#       if user_guess == actual_answer:
#       print(" you win")
#       elif user_guess > actual_answer:
#       print("Too high")
#       print("Guess again")
#       elif user_guess < actual_answer:
#       print("Too low")
#       print("Guess again")
#       else:
#       print("You've run out of guesses, you lose.")
#
#   print(f" You have {_} attempts remaining to guess the number")
