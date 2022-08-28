class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

# "getter" instance method to
    @property
    def balance(self):
        return self._balance


def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")


if __name__ == "__main__":
    main()
