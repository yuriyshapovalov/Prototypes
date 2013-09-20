# projecteuler.net/problem=206
from decimal import *

def main():
    answer = ConcealedSquare()
    print("Answer: {}".format(answer))

def ConcealedSquare():
    getcontext().prec = 22
    i = 1
    while True:
        i += 1
        s = str(Decimal(i).sqrt())

        a = s.split(sep='.')
        if len(a) > 1:
            el = str(a[0]) + str(a[1])
            #print(el)

            if el[0] == '1' and el[2] == '2' and el[4] == '3' and el[6] == '4' and el[8] == '5' and el[10] == '6' and el[12] == '7' and el[14] == '8' and el[16] == '9' and el[18] == '0': 
                return i
        

if __name__ == '__main__':
    main()
