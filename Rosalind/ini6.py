# rosalind.info/problems/ini6
import sys

def main(filename):
    f = open(filename, 'r')
    s = f.readline()
    words = s.split()
    d = {}
    for w in words:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1

    for i in d:
        print("{0} {1}".format(i, d[i]))

if __name__ == '__main__':
    main(sys.argv[1])
