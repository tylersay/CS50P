class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard): #inherit from Wizard superclass
    def __init__(self, name, house):
        super().__init__(name) #access superclass' initialization method
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")