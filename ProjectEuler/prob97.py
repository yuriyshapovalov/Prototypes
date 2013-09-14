# projecteuler.net/problem=97

def main():
    answer = NonMersennePrime()
    print(answer)

def NonMersennePrime():
    res = 28433 * pow(2, 7830457) + 1
    return res

if __name__ == '__main__':
    main()
