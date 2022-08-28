def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # at least 2 char, max 6 char
    if 2 <= len(s) <= 6:

        # no period, space, punctuation
        if s.isalnum():

            # first 2 char are letters
            if s[0:2].isalpha:

                # numbers cannot be in middle, must be end
                # num cannot start with zero
                i = 0
                while i < len(s):
                    if s[i].isdigit():
                        if s[i] != "0" and s[i:].isdigit():
                            break
                        else:
                            return False
                    else:
                        i += 1



                return True





main()