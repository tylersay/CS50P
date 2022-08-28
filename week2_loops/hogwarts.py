students = [
    {"name": "Hermoine", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]

for i in range(len(students)):
    print(i + 1, students[i])

for stud in students:
    print(stud["name"], stud["house"], stud["patronus"], sep=", ")