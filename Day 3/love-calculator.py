your_name = input('What is your name?\n')
other_name = input('What is his/her name?\n')

combined_name = (your_name + other_name).lower()

first_check_characters = ['t', 'r', 'u', 'e']
second_check_characters = ['l', 'o', 'v', 'e']

first_check_characters_count = 0
second_check_characters_count = 0

for character in first_check_characters:
    first_check_characters_count += combined_name.count(character)

for character in second_check_characters:
    second_check_characters_count += combined_name.count(character)

love_score = first_check_characters_count * 10 + second_check_characters_count

if love_score < 10 or love_score > 90 :
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 40 <= love_score <= 50 :
    print(f'Your score is {love_score}, you are alright together.')
else :
    print(f'Your score is {love_score}.')

