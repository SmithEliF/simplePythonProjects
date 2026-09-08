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

# Set it up to only print score if its the second time or more through the loop

    firstTime = True
    score = 0

    while gameloop:

# Keep the screen clean

        os.system('clear')
        print(logo)

# Choose two people at random from the data list to compare

        person1 = data[random.randint(0, len(data) - 1)]
        person2 = data[random.randint(0, len(data) - 1)]

# Make sure the two people are not the same person

        if person1 == person2:
            continue

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

startGame()