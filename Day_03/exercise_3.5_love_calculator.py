"""
You are going to write a program that tests the compatibility between two people. 
To work out the love score between two people:
* Take both people's names and check for the number of times the letters in the word TRUE occurs.
* Then check for the number of times the letters in the word LOVE occurs.
* Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
* "Your score is *x*, you go together like coke and mentos."
* For Love Scores between 40 and 50, the message should be:
* "Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is *z*."

"""
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1.lower() + name2.lower()

T = name.count('t')
R = name.count('r')
U = name.count('u')
E = name.count('e')
score_one = T + R + U + E
L = name.count('l')
O = name.count('o')
V = name.count('v')
score_two = L + O + V + E

score = int(str(score_one) + str(score_two))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")