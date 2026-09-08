from art import logo
import os
import random

# Clear the terminal screen

os.system("clear")

# Initialize the difficulties for the failsafe

difficulties = ["easy", "hard"]

def gameStart():

# Initialize the random number to be guessed

    number = random.randint(1, 100)

# Welcome the player in the game and ask for the difficulty level

    print(logo)
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # Failsafe in case the player inputs an invalid difficulty level

    if difficulty not in difficulties:
        os.system("clear")
        gameStart()

    else:

# Set the number of lives based on the difficulty level

        if difficulty == "easy":
            lives = 10
        else:
            lives = 5

# Game loop that continues until the player runs out of lives or guesses the number correctly

        while lives > 0:
            print(f"You have {lives} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high.\nGuess again.")
                lives -= 1
            elif guess < number:
                print("Too low.\nGuess again.")
                lives -= 1
            else:
                print(f"You got it! The answer was {number}.")
                break

gameStart()