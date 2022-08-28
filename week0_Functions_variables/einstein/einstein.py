def main():
    mass = int(input("m: "))

    print(emc2(mass))

def emc2(mass):
    return mass * 300000000 * 300000000

main()