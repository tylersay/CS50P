class Student:
    def __init__(self, name, house): #patronus):
        self.name = name
        self.house = house
        # self.patronus = patronus

    #when another function calling student expects a STRING from this class
    def __str__(self):
        return f"{self.name} from {self.house}"

    # functionality to get student is nested into class methods
    # related function to class, neater
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name.")
        else:
            self._name = name
    # Getter
    @property
    def house(self):
        #add underscoRe to instance variable because it clashes with property(function in a class)
        return self._house
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦦"
    #         case _:
    #             return "🪄"

def main():
    student = Student.get() #classmethod
    print(student)
    # print(student.charm())



    ###################
    # # creating an object from classes
    ###################
    # student = Student()
    # student.name = input("name: ")
    # student.house = input("house: ")
    # return student

if __name__ == "__main__":
    main()