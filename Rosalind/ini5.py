# rosalind.info/problems/ini5
import sys

def main(filename):
    i = 1
    f = open(filename, 'r')

    s = ''
    for line in f:
        if i % 2 == 0:
            s += line
        i += 1
    print(s)

if __name__ == '__main__':
    main(sys.argv[1])
