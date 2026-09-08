import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

prompts = ['espresso','latte','cappuccino','report','off']

machineOn = True

def prompt():

    clearScreen()

    return input("What would you like? (espresso/latte/cappuccino/report): ")

def powerOff():
    """Powers off the machine"""
    exit()

def report():
        """Prints out the resources"""
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

def resoureceCheck(drinkIngredients):
     """Makes sure the machine has enough resources"""
     for resource in drinkIngredients:
          if drinkIngredients[resource] > resources[resource]:
                print(f"Sorry there is not enough {resource}")
                return False
          return True
     
def processCoins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def clearScreen():
     """Clears the screen"""
     os.system('clear')

def transactionSuccess(moneyReceived, drinkCost):
        if moneyReceived >= drinkCost:
            change = round(moneyReceived - drinkCost, 2)
            print(f"Here is ${change} in change.")
            global profit
            profit += drinkCost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False


def makeCoffee(drinkName, orderIngredients):
    """Deduct the required ingredients from the resources."""
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName} ☕️. Enjoy!")

def waitForInput():
    input("Press enter to continue: ")

# Loops through while machine is on

while machineOn:
    request = prompt()
    if request == "off":
        powerOff()
    elif request == "report":
        report()
        waitForInput()
    elif request in MENU:
        drink = MENU[request]
        if resoureceCheck(drink["ingredients"]):
            payment = processCoins()
            if transactionSuccess(payment, drink['cost']):
                makeCoffee(request, drink["ingredients"])
                waitForInput()
    else:
        print("Choose a valid option")

