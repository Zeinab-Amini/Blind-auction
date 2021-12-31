from replit import clear
from art import logo
print(logo)

name_and_bid = {}
#not true but False!!!!
any_others = False

#did not even start on this part
def hightest_bidder(bidding_record):
    #trying to look at each one and see which one is the highest
    for bidder in bidding_record:
        high = 0
        winner = ""
        bid_amount = bidding_record[bidder]
        if bid_amount > high:
            bid_amount = high
            winner = bidder
    print(f"The winner is {winner} with the bid of ${high}")
        

while any_others == True:
    #correct with the while loop
    name = input("Type your name here: ")
    bid = int(input("Type your bid here: $"))
    #wrongly created dictionary
    name_and_bid[name] = bid
    #forgot to save it into a varible
    should_conitue = input("Are there any other biders? 'yes' or 'no': ")
    if should_conitue == 'no':
        any_others = True
        hightest_bidder(bid)
    elif should_conitue == 'yes':
        clear()
    