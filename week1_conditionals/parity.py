def main():
    x = int(input("what is x? "))


    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    return n % 2 == 0



main()