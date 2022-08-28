def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    while True:
        try:
            i, j = fraction.split("/")
            percentage = round(int(i) / int(j) * 100)
            # if percentage > 100:
            #     raise ValueError
        except (ValueError, ZeroDivisionError):
            raise
        else:
            return percentage


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
