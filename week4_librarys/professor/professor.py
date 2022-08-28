import random



def main():
    numof_problems = 10
    numof_tries = 3
    score = 0

    level = get_level()
# checks number of questions asked
    while numof_problems > 0:
        numof_problems -= 1
        print(f"problems: {numof_problems}")
        x, y = generate_integer(level)
        answer = question(x, y, numof_tries)
        if answer == True:
            score += 1
        print(f"score is: {score}")
    return score



def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level
            else:
                get_level()

#################
# well isnt this elegant
#################
def generate_integer(level):
    x = "0"
    y = "0"
    while level > 0:
        x = x + (str(random.randint(0, 9)))
        y = y + (str(random.randint(0, 9)))
        level -= 1
    return int(x), int(y)


def question(x, y, numof_tries):
    while numof_tries > 0:
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans ==  x + y:
                return True
            else:
                numof_tries -= 1
                print("num of tries", {numof_tries})
                print("wrong ans EEE")
        except ValueError:
            numof_tries -= 1
            print("problem EEE")
    else:
        print(f"{x} + {y} = {x + y}")
        return False



if __name__ == "__main__":
    main()
