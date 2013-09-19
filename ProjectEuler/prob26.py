# projecteuler.net/problem=26
from decimal import *

def main():
    answer = ReciprocalCycles()
    print("\nAnswer: {}".format(answer))

def ReciprocalCycles():
    getcontext().prec = 80
    for i in range(1, 100):
        print(Decimal(1)/Decimal(i))

if __name__ == '__main__':
    main()
