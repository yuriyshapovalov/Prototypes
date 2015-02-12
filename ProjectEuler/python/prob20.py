# projecteuler.net/problem=20

def main():
    answer = FactorialDigitSum(10)
    print(answer)

def FactorialDigitSum(n):
    factorial = Factorial(100)
    res = 0
    str_fac = str(factorial)
    for i in range(0, len(str_fac)):
        res += int(str_fac[i])
    return res

def Factorial(n):
    if n <= 1:
        return 1
    else:
        return n * Factorial(n-1)

if __name__ == '__main__':
    main()
