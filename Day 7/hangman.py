import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
lives_remaining = 6
print(f"lives Remaining : {lives_remaining}")

display = []
for _ in range(chosen_word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives_remaining -= 1
        print(f"{stages[lives_remaining]}")
        if lives_remaining == 0:
            end_of_game = True
            print("You Lose")

    if "_" not in (display):
        end_of_game = True
        print("You Win")
