import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def chooseAsci(type):
    if type == 0:
        return rock
    elif type == 1:
        return paper
    elif type == 2:
        return scissors


person_choose_input = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. "
)

person_choose = int(person_choose_input)
print(f"You Choose {chooseAsci(person_choose)}")
computer_choose = random.randint(0, 2)
print(f"Computer Choose {chooseAsci(computer_choose)}")


if person_choose == computer_choose:
    print("Match Draw")
elif person_choose == 0 and computer_choose == 2:
    print("You Win")
elif person_choose == 2 and computer_choose == 1:
    print("You Win")
elif person_choose == 1 and computer_choose == 0:
    print("You Win")
elif person_choose == 0 and computer_choose == 1:
    print("You Lose")
elif person_choose == 1 and computer_choose == 2:
    print("You Lose")
elif person_choose == 2 and computer_choose == 0:
    print("You Lose")
else:
    print("Invalid Number! You lose")
