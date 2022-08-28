# x = float(input("What is x? "))
# y = float(input("What is y? "))
# operator = input("What operator? ")

# if (operator == "+"):
#     z = x + y
# elif (operator == "-"):
#     z = x - y
# elif (operator == "/"):
#     z = x / y
# elif (operator == "*"):
#     z = x * y

# z = round(z, 2)
# print(f"{z:,}")

def main():
    x = int(input("what is x? "))

    print("x squared is", square(x))


def square(num):
    return (num * num)

main()