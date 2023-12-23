#Step 5
import random
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#Testing code
print(f"The chosen word is {chosen_word} ")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
#print(display)
#end_of_game = False
# print("generate as many blanks as letter in word")
    guess = input("Guess a letter: ").lower()
    print("is the guessed letter in the word ?\n")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position:{position} \n Current letter:{letter}\n Guessed letter:{guess}")
        if letter == guess:
            display[position] = letter
        else:
            print("No match")
        # TODO-2: - If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."

        # Join all the elements in the list and turn it into a String.
        if guess not in chosen_word:
          lives -= 1
          if lives == 0 :
            end_of_game= True
            print("You lose.")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
          end_of_game=True
          print("you win. ")
        #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        print(stages[lives])


 #     print("Right")
 #        display[position] = letter
 # else:
 #     print("wrong")
#     print("replace the blank with the letter")
#     "are all the blanks filled?"
# else:
#     print("lose a life")
# if have they run out=yes
#     gaveover
# else
#    ask the user to guess a letter
