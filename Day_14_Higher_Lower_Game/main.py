import random
from art import logo, vs
from game_data import data


def random_celeb():
    return random.choice(data)


def info_string(celeb_dict):
    return f"{celeb_dict['name']}, {celeb_dict['description']}, from {celeb_dict['country']}."


def insta_follow_count(celb_dict):
    return celb_dict['follower_count']


def compare_celebs(guess, celeb_a, celeb_b):
    if celeb_a > celeb_b:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    continue_game = True
    celeb_a = random_celeb()
    celeb_b = random_celeb()

    while continue_game:
        celeb_a = celeb_b
        celeb_b = random_celeb()

        while celeb_a == celeb_b:
            celeb_b = random_celeb()
        print(info_string(celeb_a))
        print(vs)
        print(info_string(celeb_b))

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = insta_follow_count(celeb_a)
        b_followers = insta_follow_count(celeb_b)
        is_correct = compare_celebs(user_guess, a_followers, b_followers)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            continue_game = False
            print(f"You' wrong! Final score is: {score}")


game()