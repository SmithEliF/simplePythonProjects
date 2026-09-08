import os
from art import logo
from art import vs
from gameData import data
import random

os.system('clear')

# Initialize failsafe

CHOICES = ['A', 'B']

# Set up game loop

gameloop = True

def startGame():

    firstTime = True
    score = 0

    while gameloop:

        os.system('clear')
        print(logo)

        person1, person2 = choosePeople()

# Only print score if its not the first time through the loop

        if not firstTime:
            print(f"You're right! Current score: {score}.")

# Print the two people to compare and ask for input

        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
        print(vs)
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

# Check if the input is valid and if the user guessed correctly

        if choice in CHOICES:
            if (person1['follower_count'] > person2['follower_count'] and choice == 'A') or (person1['follower_count'] < person2['follower_count'] and choice == 'B'):
                print("good job")
                score += 1
                firstTime = False

# Print if the user got it wrong and break the loop to end the game
    
            else:
                print("Sorry, that's wrong. Final score: " + str(score))
                break

# failsafe for invalid input

        else:
            print("Choose A or B only")
            continue

def choosePeople():
    person1 = data[random.randint(0, len(data) - 1)]
    person2 = data[random.randint(0, len(data) - 1)]
    if person1 == person2:
        choosePeople()
    return person1, person2

startGame()