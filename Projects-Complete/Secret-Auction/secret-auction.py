import secret_auction_art
import os

print(secret_auction_art.logo)
print("Welcome to the secret auction")
more_bidders = True
price_dict = {}
duplicate_name_counter = 0
while more_bidders:
    name = str(input("What is your name?: "))
    bid = str(input("What is your bid?: "))
    if "$" in bid:
        bid = int(bid.replace("$", ""))
    else:
        bid = int(bid)
    if name not in price_dict:
        price_dict[name] = bid
    else:
        name = name + str(duplicate_name_counter)
        duplicate_name_counter += 1
        price_dict[name] = bid

    still_bidders = input("Are there other users who want to bid? Type 'yes' or 'no'. ").lower()
    if still_bidders == "no":
        more_bidders = False
    else:
        os.system('cls')

os.system('cls')
max_bidder = max(price_dict, key=price_dict.get)
print(f"The winner is {max_bidder} with a bid of ${price_dict[max_bidder]}.")