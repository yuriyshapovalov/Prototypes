#projecteuler.net/problem=12
from math import sqrt

def main():
    answer = DivisibleTriangularNum()
    print("Answer: {}".format(answer))

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
    count = 1
    i = 1
    while i <= (n/2)+1:
        if n % i == 0:
            count += 1
        i += 1
    return count

if __name__ == '__main__':
    main()
