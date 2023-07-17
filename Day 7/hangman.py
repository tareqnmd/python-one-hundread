import random
import os

from hangman_arts import logo, stages
from hangman_words import word_list

print(f"{logo}\n")
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
lives_remaining = 6
print(f"lives Remaining : {chosen_word,lives_remaining}")

display = []
for _ in range(chosen_word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    if guess in display:
        print(f"You already guessed {guess}")
    else:
        for position in range(chosen_word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    if guess not in chosen_word:
        lives_remaining -= 1
        print(
            f"you guessed {guess}, that's not in the word. you lose a life. Remaining life : {lives_remaining}"
        )
        if lives_remaining == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in (display):
        end_of_game = True
        print("You Win")

    print(f"{stages[lives_remaining]}")
