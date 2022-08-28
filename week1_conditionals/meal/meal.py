def main():
    ask_time = input("what time is it? ")
    if 7 <= convert(ask_time) <= 8:
        print("breakfast time")
    elif 12 <= convert(ask_time) <= 13:
        print("lunch time")
    elif 18 <= convert(ask_time) <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return (float(hours) + float(minutes)/int(60))


if __name__ == "__main__":
    main()