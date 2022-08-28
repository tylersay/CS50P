#########################
# using CSV reader module
#########################
import csv

name = input("what is your name? ")
home = input("home? ")

with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name" :name, "home": home})







#########################
# using CSV reader module
#########################
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"], "house": row["house"]})

# for student in sorted(students, key=lambda student: student['name']):
#     print(f"{student['name']} was from {student['home']}")

# print(students)


#########################
# house
#########################

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)



# # list of students with dictionary of key-value pairs
# for student in sorted(students, key= lambda student: student['name']):
#     print(f"{student['name']} is in {student['house']}")

# print(students)



