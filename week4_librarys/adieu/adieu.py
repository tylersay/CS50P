import inflect
p = inflect.engine()

def main():
    my_names = get_names()


    print(f"Adieu, adieu, to {p.join(my_names)}")



def get_names():
    my_names = []
    while True:
        try:
            name = input("Name: ").title()
        except EOFError:
            return my_names
        else:
            my_names.append(name)



main()