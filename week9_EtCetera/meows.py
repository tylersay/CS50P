# class Cat:
#     def __init__(self, MEOWS):
#         self.MEOWS = MEOWS

#     def meow(self):
#         for _ in range(self.MEOWS):
#             print("meow")

# cat = Cat(3)
# cat.meow()


#################
## type hint:
# run with cmd: mypy meows.py
# error will show type errors
#################
# def meow(n: int) -> str: #n shld be int, output shld be str
#     #third-party tools detect """docstrings""", it can automatically create documentation
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A sting of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")


#################
## argparse library
# parse command-line agrs
#################
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default= 1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("Meow")