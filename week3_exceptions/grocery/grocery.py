def main():
    my_list = add_to_list()
    sorted_list = dict(sorted(my_list.items(), key=lambda x: x[0].lower()))
    for item in sorted_list:
        print(f"{sorted_list[item]} {item}")

def add_to_list():
    my_list = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            return my_list
        else:
            if item in my_list:
                my_list[item] += 1
            else:
                my_list[item] = item
                my_list[item] = 1

main()