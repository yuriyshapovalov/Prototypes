# projecteuler.net/problem=10

def main():
    answer = SumOfPrimes(2000000)
    print(answer)

def SumOfPrimes(n):
	i = n-1
	res=0
	while i > 1:
		if isPrime(i):
			print(i)
			res += i
		i -= 1
	return res

def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    main()
