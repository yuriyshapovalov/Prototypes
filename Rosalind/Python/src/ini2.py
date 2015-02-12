# rosalind.info/problems/ini2

import sys

def main(a, b):
    x = int(a) if a != '' else 0
    y = int(b) if b != '' else 0
    print(x*x + y*y)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
