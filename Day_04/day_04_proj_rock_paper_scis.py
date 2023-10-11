rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rps = [rock, paper, scissors]

computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("Your choice:")
    print(rps[user_choice])
    print("Computer choice:")
    print(rps[computer_choice])
    # Rules
    # * Rock wins against Scissors
    # * Scissors wins against  paper
    # * Paper wins against rock.

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 1 and computer_choice ==0:
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == computer_choice:
        print("Its draw")
    else:
        print("You lose")