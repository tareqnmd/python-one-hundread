list = [1, 2, 3, 4, 5]
new_list = [item * item for item in list]
print(list, new_list)

name = "Tareq"
new_name = [letter for letter in name]
print(name, new_name)

range_list = [item * 2 for item in range(1, 5)]
print(range_list)

range_list_updated = [item * 2 for item in range(1, 5) if item % 2 == 0]
print(range_list_updated)
