import random

input_persons = input("Please enter the persons : ")

persons_list = input_persons.split(",")
persons_list_length = len(persons_list)
random_person_index = random.randint(0, persons_list_length - 1)

picked_person = persons_list[random_person_index]

result = f"{picked_person} is selected for today bill."

print(result)
print(random.choice(persons_list))
