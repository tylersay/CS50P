# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()

##############
# MAP
##############
# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = map(str.upper, words)
#     print(*uppercased)

# if __name__ == "__main__":
#     main()

############################
# list comprehensions
############################
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()