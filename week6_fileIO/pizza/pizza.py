import csv
from tabulate import tabulate
import sys

def main():
    check_args()
    menu = open_csv()
    # print(menu)

    print(tabulate(menu, headers="firstrow", tablefmt="grid"))

    # menu = []
    # with open(sys.argv[1], "r") as csvfile:
    #     reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row)



def open_csv():
    menu = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                menu.append(row)
                # print(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return menu


def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a Python file")
    else:
        return True






if __name__ == "__main__":
    main()