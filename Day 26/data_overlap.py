with open("./Python 1-100/Day 26/file1.txt") as file1:
    file1_list = file1.readlines()
with open("./Python 1-100/Day 26/file2.txt") as file2:
    file2_list = file2.readlines()

result = [int(num) for num in file1_list if num in file2_list]
print(result)
