import random
import statistics
import sys

coin = random.choice(["heads", "tails"])
print(coin)

###############
#  get a random number from 1 to 10
###############
number = random.randint(1, 10)
print(number)

###############
# shuffle order
###############
cards = ["jack", "queen", "king", 10, "ace"]
random.shuffle(cards)
for card in cards:
    print(card)

###############
#stats library
###############
print(statistics.mean([90, 100]))

###############
# command-line arguements,using:
#   sys.argv
#   sys.exit
###############
if len(sys.argv) < 2:
    sys.exit("too few arg")
for arg in sys.argv[1:]:
    print("hello my name is", arg)


