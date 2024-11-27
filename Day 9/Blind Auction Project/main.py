from art import logo

print(logo)

def bid_comparison(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

still_playing = True
all_bids = {}

while still_playing is True:
    name = input("What's your name?\n")
    price = int(input("What's you bid? \n"))
 
    all_bids[name] = price

    should_continue = input("There are others user to bid? Type 'yes' or 'no'. \n").lower()

    if should_continue == 'no':
        still_playing = False
        bid_comparison(all_bids)
    elif should_continue == 'yes':
        print("\n" * 20)

    


