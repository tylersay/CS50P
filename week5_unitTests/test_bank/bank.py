def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greet):
    greet = greet.strip().lower()
    if greet.startswith("hello"):
        return int(0)
    elif greet[0] == "h":
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()