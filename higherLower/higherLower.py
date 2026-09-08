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

        screenClear()

        person1, person2 = choosePeople()

# Compares people

        def formatInformation():
                """Formats the information of a person for printing."""
                name1 = person1['name']
                name2 = person2['name']
                desc1 = person1['description']
                desc2 = person2['description']
                country1 = person1['country']
                country2 = person2['country']
                def comparePeople():
                        """Compares between two people and prints their information."""
                        print(f"Compare A: {name1}, a {desc1}, from {country1}.")
                        print(vs)
                        print(f"Compare B: {name2}, a {desc2}, from {country2}.")

                comparePeople()
        
# Only print score if its not the first time through the loop

        if not firstTime:
            print(f"You're right! Current score: {score}.")

# Print the two people to compare and ask for input

        formatInformation()

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

# Chooses people

def choosePeople():
    """Choose two random people from the data list and return them."""
    person1 = data[random.randint(0, len(data) - 1)]
    person2 = data[random.randint(0, len(data) - 1)]
    if person1 == person2:
        choosePeople()
    return person1, person2

# Clears the screen

def screenClear():
    """Clears the screen and prints the logo."""
    os.system('clear')
    print(logo)

startGame()