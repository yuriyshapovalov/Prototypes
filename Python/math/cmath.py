# cmath - mathematical functions for complex numbers
import cmath

def main():
    a = complex(-1.0, 0.73)
    b = complex(1.2, 3.4)

    # conversion from/to polar coordinates
    print("Conversion to and from polar coordinates")

    y = cmath.phase(a)
    print("math.phase({}) = {}".format(a, y))

    y = cmath.polar(b)
    print("math.polar({}) = {}".format(b, y))

    y = cmath.rect(5, 8.31)
    print("math.rect(5, 8.31) = {}".format(y))

if __name__ == '__main__':
    main()
