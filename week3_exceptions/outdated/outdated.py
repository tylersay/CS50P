def main():
    word_months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    month, day, year = ask_date(word_months)

    print(f"{year}-{month:02d}-{day:02d}")


def ask_date(word_months):
    while True:
        try:
            date = input("Date: ").strip()
            if date[0].isdigit():
                month, day, year = number_date(date)
                if month > 12 or day > 31:
                    ask_date(word_months)
            elif date[0].isalpha():
                month, day, year = words_date(date, word_months)
                if month > 12 or day > 31:
                    ask_date(word_months)

        except (TypeError, ValueError):
            pass
        else:
            return month, day, year


def number_date(date):

    mm, dd, yyyy = date.split("/")
    # if (mm <= 12) and (dd <= 31):
    return int(mm), int(dd), int(yyyy)


def words_date(date, word_months):

    mm, dd, yyyy = date.split(" ")
    dd = dd.removesuffix(",")
    if mm.title() in word_months:
        mm = (int(word_months.index(mm)) + 1)
        # print(f"{mm}")
        # if mm <= 12 and dd <= 31:
        return int(mm), int(dd), int(yyyy)


main()
