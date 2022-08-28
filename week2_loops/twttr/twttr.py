def main():
    user_input = input("Input: ")
    remove_vowels(user_input)

def remove_vowels(words):
    for letter in words:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            print("", end="")
        else:
            print(letter, end="")
    print()
main()