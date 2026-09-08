from art import logo
import os

os.system('clear')

# Print title screen

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encode and decode function

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

# For loop that goes through each letter in the original_text and shifts it foreward

        if letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

# If the character is not a letter just add it back

        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

goAgain = True

while goAgain:

# User inputs

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# Replayability

    if(input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")) == "yes":
        goAgain = True
    else:
        goAgain = False


