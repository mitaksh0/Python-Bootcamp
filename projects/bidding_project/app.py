import os
import art

# finds and prints highest bid winner.
def find_highest_bidder(bidding_ingo):
    # TODO-4: Compare bids in dictionary
    highest_bid = 0
    highest_bidder = ""
    for bid in bidding_ingo:
        for key in bid:
            if bid[key] > highest_bid:
                highest_bid = bid[key]
                highest_bidder = key

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
    

bidder_info = []
bid_continue = True
print(art.logo)

while bid_continue:
    
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    # TODO-2: Save data into dictionary {name: price}
    bidder_info.append({name:bid})
    
    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    # clear screen
    print("\n" * 100)

    if more_bidders == 'no':
        bid_continue = False
        find_highest_bidder(bidder_info)

