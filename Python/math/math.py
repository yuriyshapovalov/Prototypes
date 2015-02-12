# math
import sys
import math

def main():
    a = 5.873
    b = 4
    c = -2.7

    # number-theoretic and representation functions
    # https://docs.python.org/2/library/math.html#number-theoretic-and-representation-functions
    print("\nNumber-theoretic and representation functions")

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

    y = math.fmod(a, b)
    print("math.fmod({}, {}) = {}".format(a, b, y))

    (y, z) = math.frexp(c)
    print("math.frexp({}) = ({}, {})".format(c, y, z))

    y = math.fsum([.1,.2,.3,.4,.5,.6,.7,.8,.9])
    print("math.fsum([.1,.2,.3,.4,.5,.6,.7,.8,.9]) = {}".format(y))

    y = math.isfinite(a)
    print("math.isfinite({}) = {}".format(a, y))

    y = math.isinf(a)
    print("math.isinf({}) = {}".format(a, y))

    y = math.isnan(c)
    print("math.isnan({}) = {}".format(c, y))

    y = math.ldexp(c, b)
    print("math.ldexp({}, {}) = {}".format(c, b, y))

    y = math.modf(a)
    print("math.modf({}) = {}".format(a, y))

    y = math.trunc(a)
    print("math.trunc({}) = {}".format(a, y))

    # Power and logarithmic functions
    print("\nPower and logarithmic functions")

    y = math.exp(b)
    print("math.exp({}) = {}".format(b, y))

    y = math.expm1(b)
    print("math.expm1({}) = {}".format(b, y))

    y = math.log(a)
    print("math.log({}) = {}".format(a, y))

    y = math.log1p(a)
    print("math.log1p({}) = {}".format(a, y))

    y = math.log2(a)
    print("math.log2({}) = {}".format(a, y))

    y = math.log10(a)
    print("math.log10({}) = {}".format(a, y))

    y = math.pow(a, b)
    print("math.pow({}, {}) = {}".format(a, b, y))

    y = math.sqrt(b)
    print("math.sqrt({}) = {}".format(b, y))

    # Trigonometric functions
    print("\nTriginometric functions")

    a = 0.24235
    b = 0.5953

    y = math.acos(a)
    print("math.acos({}) = {}".format(a, y))

    y = math.asin(a)
    print("math.asin({}) = {}".format(a, y))

    y = math.atan(a)
    print("math.atan({}) = {}".format(a, y))

    y = math.atan2(a,b)
    print("math.atan2({},{}) = {}".format(a, b, y))
    
    a = 90
    b = 15

    y = math.sin(a)
    print("math.sin({}) = {}".format(a, y))

    y = math.cos(a)
    print("math.cos({}) = {}".format(a, y))

    y = math.tan(a)
    print("math.tan({}) = {}".format(a, y))

    y = math.hypot(a, b)
    print("math.hypot({}, {}) = {}".format(a, b, y))

    # Angular conversion
    print("\nAngular conversion")

    a = 0.83

    y = math.degrees(a)
    print("math.degrees({}) = {}".format(a, y))

    y = math.radians(b)
    print("math.radians({}) = {}".format(b, y))

    # Hyperbolic functions
    print("\nHyperbolic functions")

    a = 90

    y = math.acosh(b)
    print("math.acosh({}) = {}".format(b, y))

    y = math.asinh(a)
    print("math.asinh({}) = {}".format(a, y))

    y = math.atanh(0.53)
    print("math.atanh({}) = {}".format(0.53, y))

    y = math.cosh(b)
    print("math.cosh({}) = {}".format(b, y))

    y = math.sinh(a)
    print("math.sinh({}) = {}".format(a, y))

    y = math.tanh(b)
    print("math.tanh({}) = {}".format(b, y))

    # Special functions
    print("\nSpecial functions")

    a = 34

    y = math.erf(a)
    print("math.erf({}) = {}".format(a, y))

    y = math.erfc(a)
    print("math.erfc({}) = {}".format(a, y))

    y = math.gamma(a)
    print("math.gamma({}) = {}".format(a, y))

    y = math.lgamma(a)
    print("math.lgamma({}) = {}".format(a, y))

if __name__ == '__main__':
    main()
