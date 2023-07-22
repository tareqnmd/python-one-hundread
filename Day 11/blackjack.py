import random

from art import logo

begin = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_blackjack = True


def get_new_card(already_cards):
    filter_cards = list(filter(lambda x: x not in already_cards, cards))
    print(random.choice(filter_cards))
    return random.choice(filter_cards)


if begin == "y":
    print(logo)
    while play_blackjack:
        player_cards = random.choices(cards, k=2)
        computer_cards = random.sample(cards, 2)
        player_cards_total = sum(player_cards)
        print(f"    Your cards: {player_cards}, current score is: {player_cards_total}")
        print(f"    Computer's first card: {computer_cards[0]}")
        computer_another_card_decision = bool(random.getrandbits(1))
        # computer_another_card_decision = random.choice([True, False])
        if computer_another_card_decision:
            computer_cards.append(get_new_card(computer_cards))
        player_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_another_card == "y":
            player_cards.append(get_new_card(player_cards))
        continue_play = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': "
        )
        if continue_play != "y":
            play_blackjack = False
