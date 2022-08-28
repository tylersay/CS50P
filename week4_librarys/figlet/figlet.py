from pyfiglet import Figlet
figlet = Figlet()
import sys
import random

def main():

    if len(sys.argv) == 1:
        no_args()

    elif len(sys.argv) == 3:
        two_args()

    else:
        sys.exit("Invalid usage")

    s = input("Input: ")
    print(figlet.renderText(s))






def no_args():
    all_fonts = figlet.getFonts()
    numof_fonts = len(all_fonts)
    num = random.randint(1, numof_fonts)
    my_rand_font = all_fonts[num]
    figlet.setFont(font=my_rand_font)



def two_args():
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print(sys.argv[1])
        sys.exit("Invalid usage")
    f = sys.argv[2]
    all_fonts = figlet.getFonts()
    if f in all_fonts:
        figlet.setFont(font=f)
    else:
        sys.exit("Invalid usage")





main()