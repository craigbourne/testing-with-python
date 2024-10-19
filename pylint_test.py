"""This module implements a simple Caesar cipher for encoding and decoding text."""

import string

SHIFT = 3
LETTERS = string.ascii_letters + string.punctuation + string.digits

def caesar_cipher(text, mode='encode'):
    """Encode or decode text using a Caesar cipher."""
    encoded = ''
    for letter in text:
        if letter == ' ':
            encoded += ' '
        else:
            index = LETTERS.index(letter)
            if mode == 'encode':
                new_index = (index + SHIFT) % len(LETTERS)
            elif mode == 'decode':
                new_index = (index - SHIFT) % len(LETTERS)
            encoded += LETTERS[new_index]
    return encoded

def main():
    """Main function to run the Caesar cipher program."""
    choice = input("Would you like to encode or decode? ")
    word = input("Please enter text: ")

    if choice.lower() == "encode":
        result = caesar_cipher(word, 'encode')
    elif choice.lower() == "decode":
        result = caesar_cipher(word, 'decode')
    else:
        print("Invalid choice. Please choose 'encode' or 'decode'.")
        return

    print(result)

if __name__ == "__main__":
    main()
