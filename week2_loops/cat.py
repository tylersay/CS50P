def main():
    i = 0
    while (i < 3):
        print("meow")
        i += 1

    for _ in range(5):
        print("woof")

    while True:
        num = int(input("what is n? "))
        if num > 0:
            break
    print("dub dub\n" * num, end="")

main()