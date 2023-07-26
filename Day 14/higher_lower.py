import os
import random

from art import logo, vs
from game_data import data

print(logo)
score = 0
choices = random.choices(data, k=2)

first_item = choices[0]
second_item = choices[1]


def compare_info(info):
    return f"{info['name']}, a {info['description']}, from {info['country']}."


def find_result(verdict):
    if verdict == "A" and first_item["follower_count"] > second_item["follower_count"]:
        return True
    elif (
        verdict == "B" and first_item["follower_count"] < second_item["follower_count"]
    ):
        return True
    else:
        return False


print(f"Compare A: {compare_info(first_item)}")
print(vs)
print(f"Compare B: {compare_info(second_item)}")

verdict = input("Who has more followers? Type 'A' or 'B': ")
os.system("clear")

if find_result(verdict):
    print(f"You're right. Current score: {score}")
else:
    print(f"Sorry that's wrong. Final score: {score}")
