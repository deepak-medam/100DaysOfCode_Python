from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    end_text = ""
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift
            end_text += alphabet[new_position]
    print(f"The {direction}d text is {end_text}")


print(logo)
replay = True
while replay:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction, text, shift)
    play = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if play == 'no':
        replay = False
        print("Good bye")
