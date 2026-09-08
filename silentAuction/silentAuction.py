import os
from art import logo

os.system('clear')

print(logo)

biddingRound = True

bidDict = {}

highestBid = 0
winner = ""

while biddingRound:

# User input for name and bid amount

    name = input("What is your name?\n")
    price = input("What is your bid?\n")

# Validate that the bid amount is a number

    if not price.isdigit():
        print("Please enter a valid number for the bid amount.")
        continue

# Clear the console after each bid to keep the auction silent

    os.system('clear')

# Move the name and bid amount into a dictionary to keep track of all bids

    bidDict[name] = price

# End condition

    if input("Does anyone else still need to bid Y/N\n").upper() == "Y":
        os.system('clear')
        biddingRound = True
    else:
        biddingRound = False

# For loop that loops through the dictionary to find the highest bid and the winner

        for bidder in bidDict:

# Get each bid amount and compare it to the current highest bid

            bidAmount = int(bidDict[bidder])
            if bidAmount > highestBid:
                highestBid = bidAmount
                winner = bidder

# Output

print(f"The winner is {winner} with a bid of ${highestBid}")
