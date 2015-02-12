#projecteuler.net/problem=12
from math import sqrt
import time

def main():
    t1 = time.time()
    answer = DivisibleTriangularNum()
    t2 = time.time()
    print("Answer: {} \n:{}".format(answer, t2-t1))

def DivisibleTriangularNum():
    tri_num = 0
    i = 0
    while True:
        i += 1
        tri_num += i

        div_count = haveDivisors(tri_num)
        print('{0} :{1}'.format(tri_num, div_count))
        if div_count > 500:
            break
    return tri_num

def haveDivisors(n):
    nod = 0
    sq = sqrt(n)
    i = 1
    while i <= sq:
        if n % i == 0:
            nod += 2
        i += 1
    if (sq * sq == n):
        nod -= 1
    return nod

if __name__ == '__main__':
    main()
