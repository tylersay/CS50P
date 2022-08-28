from datetime import date, timedelta
import sys
import inflect
import re
p=inflect.engine()

def main():
    dob = date.fromisoformat(get_dob(input("Date of Birth: ")))
    today = date.today()
    delta = today - dob
    print(f"{p.number_to_words((delta.days * 24 * 60), andword='')} minutes".capitalize())



def get_dob(dob):
    if matches := re.search(r"^([0-9]{4})-([0-1][0-9]){1}-([0-3][0-9])$", dob):
        if 1 <= int(matches.group(2)) <= 12 and 1<= int(matches.group(3)) <=31 :
            return dob
    else:
        raise ValueError("Invalid date")



if __name__ == "__main__":
    main()