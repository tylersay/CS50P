def main():
    text = input()
    convert(text)


def convert(txt):
    txt1 = txt.replace(":)", '🙂').replace(":(", '🙁')

    print(txt1)

main()