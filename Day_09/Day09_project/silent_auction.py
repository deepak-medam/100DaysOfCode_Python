from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")
bider_info = {}


def find_highest_bidder(bidder_data):
    winner = ""
    win_value = 0
    for bidder in bidder_data:
        value = int(bidder_data[bidder])
        if value > win_value:
            winner = bidder
            win_value = value
    print(f"The winner is {winner} with a bid value of {win_value}.")

bidding = False
while not bidding: 
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bider_info[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if continue_bid == 'yes':
        os.system('cls')
    else:
        bidding = True
        find_highest_bidder(bider_info)
        