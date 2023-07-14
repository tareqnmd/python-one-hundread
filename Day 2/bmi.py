height = input("Please enter your height in m:\n")
weight = input("Please enter your weight in kg:\n")

bmi = float(weight) / float(height) ** 2

formatted_bmi = round(bmi, 2)

print(f"Your bmi is {formatted_bmi}")
