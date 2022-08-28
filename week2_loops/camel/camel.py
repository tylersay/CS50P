def main():
    camel = input("camelCase: ")
    # print("snake_case: ", end = "")
    make_snake(camel)

def make_snake(words):
    for letter in words:
        if letter.islower():
            print(letter, end="")
        else:
            print("_" + letter.lower(), end= "")
    print("")
main()