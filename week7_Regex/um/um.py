import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    numof_um = 0
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    for _ in (matches):
        numof_um +=1
    return numof_um


...


if __name__ == "__main__":
    main()