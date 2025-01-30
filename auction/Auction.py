# from art import logo
# #HINT: You can call clear() to clear the output in the console.
# print(logo)
# d = {}
# bid={}
# test = True
# while test:
#     name = input("What is your name? ")
#     price = int(input("What's your bid? $"))
#     d.__setitem__(name, price)
#     bid[name]=price
#     con = input("Any other bit here? y or n ").lower()
#     if con =='y' or con=='yes':
#         # clear()
#       pass
#     else:
#       test = False
#     # print(d)
# highest = 0
# for item in bid:
#   if bid[item]>highest:
#     highest = bid[item]
#     winner = item
# # print(highest,winner)
# print("The winner is {} with ${}.".format(winner,highest))

# from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        pass

"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 

https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076

"""
