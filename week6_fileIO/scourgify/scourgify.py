import csv
import sys


def main():
    check_args()
    before_data = open_before()
    name_list = split_firstlast(before_data)
    print(name_list)
    make_after(name_list)


def make_after(name_list):
    with open(sys.argv[2], "w") as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for person in name_list:
            writer.writerow({"first": person["first"], "last": person["last"], "house": person["house"]})


def split_firstlast(before_data):
    name_list = []
    for row in before_data:
        splitname = row["name"].split(",")
        name_list.append({"first": splitname[1].lstrip(), "last": splitname[0], "house": row["house"]})
    return name_list


def open_before():
    before = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                before.append(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        return before


def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a csv file")
    else:
        return True





if __name__ == "__main__":
    main()