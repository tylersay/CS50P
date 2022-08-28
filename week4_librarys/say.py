import cowsay
import sys
from sayings import hello

if len(sys.argv) ==2:
    cowsay.cow(f"hello, {sys.argv[1]}")

hello(sys.argv[1])