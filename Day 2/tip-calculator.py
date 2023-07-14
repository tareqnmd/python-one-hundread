print("Welcome to tip calculator")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
total_people = input("How many people to slipt the bill? ")

total_bill_float = float(total_bill)
tip_percentage_float = float(tip_percentage)
total_bill_with_tip = total_bill_float + (
    total_bill_float * (tip_percentage_float / 100)
)
total_people_int = int(total_people)

splitted_bill = total_bill_with_tip / total_people_int
# rounded_splitted_bill =round( total_bill_with_tip / total_people_int , 2)
rounded_splitted_bill = "{:.2f}".format(splitted_bill)

each_person_pay = f"Each person should pay: {rounded_splitted_bill}"
print(each_person_pay)
