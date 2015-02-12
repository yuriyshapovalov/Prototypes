# Rabbits and Recurrence Relations 
# rosalind.info/problems/fib
import sys
from math import sqrt

def main(n, k):
    pair = 0
    childs = 1
    for i in range(1, n):
        sub_child = pair * k
        pair += childs
        childs = sub_child
    print (childs + pair)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
