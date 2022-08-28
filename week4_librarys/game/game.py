import random
import sys

def main():
    rand_num = get_level()

    user_guess(rand_num)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            rand_num = random.randint(1, level)
        except ValueError:
            pass
        else:
            return rand_num


def user_guess(rand_num):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess < rand_num:
                print("Too small!")
                user_guess(rand_num)
            elif guess > rand_num:
                print("Too large!")
                user_guess(rand_num)
            else:
                print("Just right!")
                sys.exit()

main()