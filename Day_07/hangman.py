# You have to guess a word and for every wrong letter you submit you end up taking a life away from the little man
#Step 1 
import random
from hangman_art import logo, stages
from hangman_words import word_list


game_word = random.choice(word_list)
word_length = len(game_word)

end_of_game = False
lives = 6

print(logo)

#Create blanks
display = []
for letter in game_word:
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If user entered a letter they've already guessed
    if guess in display:
        print(f"you've already guessed {guess}")
    
    # Check guessed letter
    for position in range(word_length):
        letter = game_word[position]
        if letter == guess:
            display[position] = letter
    
    # Check if user is wrong
    if guess not in game_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(" ".join(display))

    # Check if user has got all letters
    if "_" not in display:
        print("You win!!")
    print(stages[lives])