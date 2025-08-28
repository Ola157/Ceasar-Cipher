from math import trunc

from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(original_text, shift_amount, encode_or_decode):

    new_text = ""
    for char in original_text:
        if char not in alphabet:
            new_text += char
        else:
            position = alphabet.index(char)
            if encode_or_decode == "encode":
                position += shift_amount
            elif encode_or_decode == "decode":
                position -= shift_amount
            position %= len(alphabet)
            new_text += alphabet[position]

    print(f"Here's the {encode_or_decode} result: {new_text}")

stop = False
while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
    if play_again != "yes":
        stop = True
        print("Good Bye")

