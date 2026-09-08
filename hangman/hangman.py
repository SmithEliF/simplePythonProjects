import random
import os

os.system('clear')

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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

wordList = ["aardvark", "baboon", "camel"]

chosenWord = random.choice(wordList)

placeholder = ""

correctLetters = []

lives = 6

# Print how many letters the word is

for letter in chosenWord:
    placeholder += "_"
    correctLetters.append("_")

print(placeholder)


while lives > 0:
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosenWord:

# If the letter is correct add it to the display

        if letter == guess:
            display += letter
            correctLetters.append(guess)

# If the letter is already guessed add it back to the display

        elif letter in correctLetters:
            display += letter

# Else keep it blank

        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You win!")
        break

    if guess not in chosenWord:
        lives -= 1
        print(stages[lives+1])

    if lives == 0:
        print("You lose!")




