# rosalind.info/problems/ini4

import sys

def main(a, b):
    a = int(a) if a != '' else 0
    b = int(b) if b != '' else 0

    if a > b:
        return

    sum = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            sum += i
    print(sum)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

