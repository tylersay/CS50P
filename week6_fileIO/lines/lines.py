import sys


def main():
    check_args()
    lines = open_pyfile()

    count_lines = 0
    for line in lines:
        if line.isspace() == False and line.lstrip().startswith("#") == False:
            count_lines += 1
    print(f"{count_lines}")


def open_pyfile():
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except (IOError, FileNotFoundError):
        sys.exit("File does not exist")
    else:
        return lines


def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        return True


if __name__ == "__main__":
    main()