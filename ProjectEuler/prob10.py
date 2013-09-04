# projecteuler.net/problem=10

def main():
    answer = SumOfPrimes(2000000)
    print(answer)

def SumOfPrimes(n):
    i = 2
    res = 0
    while i < n:
        if isPrime(i):
            
            res = res + i
        i = i + 1
    return res

def isPrime(n):
    i = n-1
    while i > 1:
        if n % i == 0:
            return False
        i = i - 1
    return True

if __name__ == '__main__':
    main()
