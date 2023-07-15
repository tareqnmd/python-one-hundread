input_results = input("Student Results\n")
input_results_split = input_results.split(",")

max = 0

for result in input_results_split:
    if max < int(result):
        max = int(result)

print(result)
