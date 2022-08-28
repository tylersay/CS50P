class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self._size + n <= self.capacity:
            self._size += n
            return self._size
        else:
            raise ValueError("Deposit exceeds capacity")

    def withdraw(self, n):
        if self._size == 0 or self._size < n:
            raise ValueError("No more cookes")
        else:
            self._size -= n
            return self._size

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
       return self._size

def main():
    jar = Jar()
    # jar.deposit(5)
    # jar.withdraw(4)
    print(jar.capacity)
    print(jar)

if __name__ == "__main__":
    main()