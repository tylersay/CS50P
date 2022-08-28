###########################
## List comprehension using conditionals
############################
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)


###########################
## filter function
############################
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


# gryffindors = filter(is_gryffindor, students)
# for gryffindor in gryffindors:
#     print(gryffindor["name"])


###########################
## Dictionary comprehension
############################
# students = ["Hermione", "Harry", "Ron"]
# ## create list with dictionary inside
# # gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
# ## create single dictionary
# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)

###########################
## Enumerate
############################
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)