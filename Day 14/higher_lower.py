import os
import random

from art import logo, vs
from game_data import data


def compare_info(info):
    return f"{info['name']}, a {info['description']}, from {info['country']}."


def find_result(verdict, a_follower, b_follower):
    if a_follower > b_follower:
        return verdict == "a"
    else:
        return verdict == "b"


def game():
    print(logo)
    score = 0
    choices = random.choices(data, k=2)
    first_item = choices[0]
    second_item = choices[1]
    game_continue = True

    while game_continue:
        while first_item == second_item:
            second_item = random.choice(data)
        print(f"Compare A: {compare_info(first_item)}")
        print(vs)
        print(f"Compare B: {compare_info(second_item)}")
        verdict = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = find_result(
            verdict, first_item["follower_count"], second_item["follower_count"]
        )
        os.system("clear")
        print(logo)

        if result:
            score += 1
            print(f"You're right. Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry that's wrong. Final score: {score}")


game()
