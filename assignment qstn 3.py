students = {
    "Ruvarashe": 97,
    "Miriam": 92,
    "Chhiedza": 78,
    "Chipo": 95,
    "Tino": 88
}

for name, mark in students.items():
    print(name, mark)

highest_mark = 0
top_student = ""

for name, mark in students.items():
    if mark > highest_mark:
        highest_mark = mark
        top_student = name

print("Top student:", top_student)
print("Highest mark:", highest_mark)

print()
