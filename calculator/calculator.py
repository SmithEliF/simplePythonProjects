import os

from art import logo

# Calculator functions

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Operation dictionary 

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():

    """
    A simple calculator that performs basic arithmetic operations.
    The user can perform multiple calculations in a single session.
    """

# Loops the calculator until the user decides to stop

    shouldAccumulate = True

# Clear the console and print the logo at the start of each calculation session

    os.system('clear')
    print(logo)

    num1 = int(input("Enter first number: "))

# Skips the num1 input if the user wants to continue with the previous result

    while shouldAccumulate:

        for symbol in operations:
            print(symbol)

        operation = input("Enter operation: ")
        operationSymbol = operation

# Validate that the operation is valid and perform the calculation

        if operation in operations:

# Choose which operation to perform based on user input and get the second number

            operation = operations[operation]
            num2 = int(input("Enter second number: "))

# Perform the calculation and display the result

            result = operation(num1, num2)
            print(f"{num1} {operationSymbol} {num2} = {result}")

# Ask the user if they want to continue with the previous result or start a new calculation

            if(input("Would you like to keep working with the previous result? y/n\n").lower()) == "y":
                shouldAccumulate = True
                num1 = result
            else:
                calculator()

# Failsafe for invalid operation input and restarts the calculator

        else:
            os.system("clear")
            print(logo)
            print("Please enter a valid operation")

# Initial start of the calculator program

calculator()
