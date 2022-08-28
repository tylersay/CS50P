def main():
    plate = input("Plate: ")
    if is_valid(plate):

        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)
    print(len(s))
    # at least 2 char, max 6 char
    if 2 > l or  l > 6:
        # print("char len")
        return False

    # no period, space, punctuation
    elif s.isalnum() == False:
        # print("alnum false")
        return False

        # first 2 char are letters
    elif s[0:2].isalpha() == False:
        # print("first 2 not alpha")
        return False

    else:
        # numbers cannot be in middle, must be end
        # num cannot start with zero
        i = 0
        while i < len(s):
            if s[i].isdigit():
                if s[i] != "0" and s[i:].isdigit():
                    return True
                else:
                    # print("num middle, num start zero")
                    return False
            else:
                i += 1
        return True


if __name__ == "__main__":
    main()
