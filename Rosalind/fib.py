# rosalind.info/problems/fib
import sys

def main(n, k):
    #tmp = fib(k)
    n = int(n)
    k = int(k)
    pair = 1
    for i in range(1, n):
        print(pair)
        pair =+ int(pair*k / 2)
    print(pair)

def fib(n):
    fb = []
    fb.append(1)
    fb.append(1)
    for i in range(1, n):
        fb.append(fb[i-1] + fb[i])
    return fb





if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
