import os
import random
from art import logo

# Clear the console

os.system("clear")

cards = {'🃑' : 'ace', '🃒' : 2, '🃓' : 3, '🃔' : 4, '🃕' : 5, '🃖' : 6, '🃗' : 7, '🃘' : 8, '🃙' : 9, '🃚' : 10, '🃛' : 10, '🃝' : 10, '🃞' : 10,
         '🃁' : 'ace', '🃂' : 2, '🃃' : 3, '🃄' : 4, '🃅' : 5, '🃆' : 6, '🃇' : 7, '🃈' : 8, '🃉' : 9, '🃊' : 10, '🃋' : 10, '🃍' : 10, '🃎' : 10,
         '🂱' : 'ace', '🂲' : 2, '🂳' : 3, '🂴' : 4, '🂵' : 5, '🂶' : 6, '🂷' : 7, '🂸' : 8, '🂹' : 9, '🂺' : 10, '🂻' : 10, '🂽' : 10, '🂾' : 10,
         '🂡' : 'ace', '🂢' : 2, '🂣' : 3, '🂤' : 4, '🂥' : 5, '🂦' : 6, '🂧' : 7, '🂨' : 8, '🂩' : 9, '🂪' : 10, '🂫' : 10, '🂭' : 10, '🂮' : 10}

playerHand = []
dealerHand = []

def calculatePlayerTotal():
    """Calculates the total value of the playerHand."""
    total = 0
    for card in playerHand:
        if cards[card] == 'ace':
            playerHand.remove(card)
            playerHand.append(card)
    for card in playerHand:
        if cards[card] == 'ace':
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += cards[card]
    return total

def calculateDealerTotal():
    """Calculates the total value of the dealerHand."""
    total = 0
    for card in dealerHand:
        if cards[card] == 'ace':
            dealerHand.remove(card)
            dealerHand.append(card)
    for card in dealerHand:
        if cards[card] == 'ace':
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += cards[card]
    return total

def dealPlayerCard():
    """Returns two random cards from the deck."""
    card = random.choice(list(cards))
    playerHand.append(card)

def dealDealerCard():
    """Returns two random cards from the deck."""
    card = random.choice(list(cards))
    dealerHand.append(card)

def gameStart():
    """Starts the game of blackjack."""
    print(logo)
    dealPlayerCard()
    dealPlayerCard()
    dealDealerCard()
    dealDealerCard()
    print(dealerHand[0], "🂠")
    print(*playerHand)
    print(f"Total: {calculatePlayerTotal()}")

gameStart()

# Hit or Stand

while True:
    choice = input(
        "Do you want to hit or stand? Type 'h' to hit or 's' to stand:\n"
    ).lower()

    if choice == "h":
        os.system("clear")
        print(logo)
        dealPlayerCard()
        print(dealerHand[0], "🂠")
        print(*playerHand)
        total = calculatePlayerTotal()
        print(f"You Chose to Hit.\nTotal: {total}")

        if total > 21:
            print("Bust! You lose.")
            break

    elif choice == "s":
        os.system("clear")
        print(logo)
        print(*dealerHand)
        print(f"Dealer Total: {calculateDealerTotal()}")
        print(*playerHand)
        total = calculatePlayerTotal()
        print(f"You Chose to Stand.\nTotal: {total}")

        if total > 21:
            print("Bust! You lose.")
        else:
            if calculateDealerTotal() < 17:
                while calculateDealerTotal() < 17:
                    os.system("clear")
                    dealDealerCard()
                    print(logo)
                    print(*dealerHand)
                    print(f"Dealer Total: {calculateDealerTotal()}")
                    print(*playerHand)
                    print(f"Total: {calculatePlayerTotal()}")
            if calculateDealerTotal() > 21:
                print("Dealer busts! You win!")
            elif calculateDealerTotal() > total:
                print("Dealer wins!")
            elif calculateDealerTotal() == total:
                print("It's a tie!")
            else:
                print("You win!")
        break

    else:
        print("Please enter 'h' or 's'.")
