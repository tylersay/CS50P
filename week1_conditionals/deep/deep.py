def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    ans = ans.strip().lower()

    is_FourTwo(ans)

def is_FourTwo(x):
    if x == "42" or x == "forty two" or x == "forty-two":
        print("Yes")
    else:
        print("No")

main()