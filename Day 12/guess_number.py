from random import randint

from art import logo

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


def check_difficulty(type):
    if type == "hard":
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS


print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = check_difficulty(difficulty)
selected_number = randint(1, 100)


while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guessed_number = int(input("Make a guess: "))
    if selected_number == guessed_number:
        print(f"You got it! The answer was {guessed_number}")
        break
    elif selected_number > guessed_number:
        print("Too Low.")
    elif selected_number < guessed_number:
        print("Too High.")
    attempts -= 1
    if attempts == 0:
        print("You are ran out of guesses, you lose.")
    else:
        print("Guess Again.")
