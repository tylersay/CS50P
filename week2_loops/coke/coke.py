def main():
    amt_due = 50
    print("Amount Due:", amt_due)

    insert_coin(amt_due)

def insert_coin(amt):
    while amt > 0:
        user_insert = int(input("Insert Coin:"))
        if user_insert == 25 or user_insert ==10 or user_insert ==5:
            amt = amt - user_insert
        else:
            print("Amount Due:", amt)
            user_insert = int(input("Insert Coin:"))
        if amt > 0:
                print("Amount Due:", amt)


    if amt <= 0:
        print("Change Owed:", abs(amt))

main()