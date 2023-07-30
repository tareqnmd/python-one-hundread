input_results = input("Student Results\n")
input_results_split = input_results.split(",")

results_length = len(input_results_split)
total_result = 0

for result in input_results_split:
    total_result += int(result)

avg_result = total_result / results_length
print(round(avg_result))
