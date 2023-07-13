current_age = input('Whats your current age : ')

current_age_float = float(current_age)
years_remaining = 90 - current_age_float
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f'you have {days_remaining} days {weeks_remaining} weeks {months_remaining} months')