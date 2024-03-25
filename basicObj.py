student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
    studentScore = student_scores[i]
    studentName = i
    if studentScore >= 91 and studentScore <= 100:
        student_scores[studentName] = "Outstanding"

    elif studentScore >= 81 and studentScore <= 90:
        student_scores[studentName] = "Exceeds Expectations"

    elif studentScore >= 71 and studentScore <= 80:
        student_scores[studentName] = "Acceptable"

    elif studentScore < 70:
        student_scores[studentName] = "Fail"

# 🚨 Don't change the code below 👇
print(student_scores)
