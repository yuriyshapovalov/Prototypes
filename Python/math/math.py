# math
import sys
import math

def main():
    a = 5.873
    b = 4
    c = -2.7

    y = math.ceil(a)
    print("math.ceil({}) = {}".format(a, y))

    y = math.floor(a)
    print("math.floor({}) = {}".format(a, y))

    y = math.copysign(a, c)
    print("math.copysign({}, {}) = {}".format(a, c, y))

    y = math.fabs(c)
    print("math.fabs({}) = {}".format(c, y))

    y = math.factorial(b)
    print("math.factorial({}) = {}".format(b, y))

if __name__ == '__main__':
    main()
