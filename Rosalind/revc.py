# rosalind.info/problems/revc
import sys

def main(s):
    res = ''
    s = s[::-1]
    lst = list(s)
    for x, i in enumerate(lst):
        if i == 'A':
            lst[x] = 'T'
        elif i == 'T':
            lst[x] = 'A'
        elif i == 'C':
            lst[x] = 'G'
        elif i == 'G':
            lst[x] = 'C'

        res += lst[x]

    print(res)


if __name__ == '__main__':
    main(sys.argv[1])
