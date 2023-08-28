import random

list = ["Tareq", "Sayma", "Helena", "Hasan"]

student_score = {student: random.randint(1, 100) for student in list}
passed_students = {
    student: score for (student, score) in student_score.items() if score >= 60
}
print(student_score, passed_students)
