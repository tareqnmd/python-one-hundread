height = input("Please enter your height in m:\n")
weight = input("Please enter your weight in kg:\n")

bmi = float(weight) / float(height) ** 2

formatted_bmi = round(bmi, 2)
bmi_result = f"Your bmi is {formatted_bmi}"


if formatted_bmi < 18.5:
    print(f"{bmi_result} (underweight)")
elif 18.5 <= formatted_bmi < 25:
    print(f"{bmi_result} (normal weight)")
elif 25 <= formatted_bmi < 30:
    print(f"{bmi_result} (overweight)")
elif 30 <= formatted_bmi < 35:
    print(f"{bmi_result} (obese)")
elif 35 <= formatted_bmi:
    print(f"{bmi_result} (clinical obese)")
