def main():
    greeting = input("Greeting: ")
    is_hello(greeting)

def is_hello(greet):
    greet = greet.strip().lower()
    if greet.startswith("hello"):
        print("$0")
    elif greet[0] == "h":
        print("$20")
    else:
        print("$100")

main()