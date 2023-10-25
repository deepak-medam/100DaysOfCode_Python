from art import logo
from random import randint

EASY_LIVES = 10
HARD_LIVES = 5
# Function to check user's guess against acutal answer.
def check_answer(guess, answer, lives):
    if guess > answer:
        print("Your guess is higher than actual number.")
        return lives - 1
    elif guess < answer:
        print("Your guess is lower than actual number")
        return lives - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_dificulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LIVES
    elif difficulty == 'hard':
        return HARD_LIVES

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    chosen_number = randint(1,100)
    user_guess = 0
    lives = set_dificulty()
    while user_guess != chosen_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        lives = check_answer(user_guess, chosen_number, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return

game()