# Enumerating Gene Orders
# rosalind.info/problems/perm
import sys
import itertools

def main(n):
    arr = [x for x in range(1, n+1)]
    res = list(itertools.permutations(arr))

    print(len(res))

    for i in res:
        r = ''
        for j in i:
            r += str(j) + ' '
        print(r)

if __name__ == '__main__':
    main(int(sys.argv[1]))
