def main():
    get_order()



def get_order():
    total_dollars = 0

    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            print(total_dollars)
            return total_dollars
        else:
            if item in menu:
                total_dollars += menu[item]

                print("$"+"{:.2f}".format(total_dollars))
main()