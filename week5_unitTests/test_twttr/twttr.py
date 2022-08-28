def main():
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):

    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in vowel:
        word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()