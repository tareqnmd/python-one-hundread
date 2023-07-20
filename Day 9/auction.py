from art import logo

print(logo)

bids = []

bid_continue = True


def get_amount(elm):
    return elm["amount"]


def winner():
    bids.sort(key=get_amount)
    winner_bid = bids[-1]
    result = f"The Winner is {winner_bid['name']} with a bid of ${winner_bid['amount']}"
    return print(result)


def add_bid(name, amount):
    new_bid = {}
    new_bid["name"] = name
    new_bid["amount"] = amount
    bids.append(new_bid)


while bid_continue:
    bidder_name = input("what's your name? ")
    bid_amount = float(input("what's your bid? $"))
    add_bid(bidder_name, bid_amount)
    next_bid = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if next_bid != "yes":
        bid_continue = False

print(winner())
