student_scores = {"Harry": 81, "Ron": 78, "Draco": 74, "Neville": 62, "Hermione": 99}


def get_grade(number):
    if 91 <= number <= 100:
        return "Outstanding"
    if 81 <= number <= 90:
        return "Exceeds Expectations"
    if 70 <= number <= 80:
        return "Acceptable"
    else:
        return "Fail"


for key in student_scores:
    student_scores[key] = get_grade(student_scores[key])

print(student_scores)
