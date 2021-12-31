from replit import clear
from art import logo
print(logo)

any_others = True

while any_others == True:
    name = input("Type your name here: ")
    bid = input("Type your bid here: ")

    name_and_bid = {
        name : bid
    }
    input("Are there any other biders? 'yes' or 'no': ")
    if any_others == 'no':
        any_others = False
        print("Wait")
    elif any_others == 'yes':
        any_others = True
        clear()
    