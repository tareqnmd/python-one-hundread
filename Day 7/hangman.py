import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
chosen_word_length = len(chosen_word)

display = []
for _ in range(chosen_word_length):
    display += "_"

for _ in range(chosen_word_length):
    guess = input("Guess a letter: ").lower()
    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

if "_" not in (display):
    print("You Win")
else:
    print("You Lose")
