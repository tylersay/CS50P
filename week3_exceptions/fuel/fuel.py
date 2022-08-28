def main():
    fraction = get_fraction("Fraction: ")
    if fraction > 100:
        get_fraction("Fraction: ")
    elif fraction >= 99:
        print("F")
    elif fraction <= 1:
        print("E")
    else:
        print(f"{fraction}%")


def get_fraction(prompt):
    while True:
        try:
            frac = input(prompt)
            i, j = frac.split("/")
            percentage = round(int(i) / int(j) * 100)
            return percentage
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break



main()