import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if matches := re.search(r"^([0-9]{1,2}):?([0-5][0-9])? (AM|PM) to ([0-9]{1,2}):?([0-5][0-9])? (AM|PM)$", s):
        hr1 = int(matches.group(1))
        hr2 = int(matches.group(4))
        if matches.group(2) != None:
            min1 = (matches.group(2))
        else:
            min1 = "00"
        if matches.group(5) != None:
            min2 = (matches.group(5))
        else:
            min2 = "00"
        am_pm1 = matches.group(3)
        am_pm2 = matches.group(6)

        if (1 <= hr1 <= 12) and (1 <= hr2 <= 12):
            hr1 = add12_or_no(hr1, am_pm1)
            hr2 = add12_or_no(hr2, am_pm2)
            # print(f"hr1: {hr1} hr2: {hr2}")
        else:
            raise ValueError
        return f"{hr1}:{min1} to {hr2}:{min2}"
    else:
        raise ValueError


def add12_or_no(hr, am_pm):
    if hr == 12 and am_pm == "AM":
        return "00"
    elif hr == 12 and am_pm == "PM":
        return hr
    elif am_pm == "PM":
        return (hr + 12)
    else:
        return f"{hr:02}"


if __name__ == "__main__":
    main()
