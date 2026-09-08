import os
from art import logo
from art import vs
from gameData import data
import random

os.system('clear')

CHOICES = ['A', 'B']
gameloop = True

def startGame():
    person1 = data[random.randint(0, len(data) - 1)]
    person2 = data[random.randint(0, len(data) - 1)]
    while gameloop:
        os.system('clear')
        print(logo)
        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
        print(vs)
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if choice in CHOICES:
            print("good job")
            
startGame()