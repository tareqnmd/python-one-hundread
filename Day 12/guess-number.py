from random import randint

from art import logo

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
selected_number = randint(1, 100)


def check_difficulty(type):
    if type == "hard":
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS


def check_number():
    guessed_number = int(input("Make a guess: "))
    if selected_number == guessed_number:
        print(f"You got it! The answer was {guessed_number}")
        return 1
    elif selected_number > guessed_number:
        print("Too Low.")
        return 0
    elif selected_number < guessed_number:
        print("Too High.")
        return 0


attempts = check_difficulty(difficulty)

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    attempts -= 1
    result = check_number()
    if result == 1:
        break
    else:
        if attempts == 0:
            print("You are ran out of guesses, you lose.")
        else:
            print("Guess Again.")
