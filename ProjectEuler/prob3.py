# projecteuler.net/problem=3

def LargestPrimeFactor():
	print('begin')
	res = FindLargestPrimeNumberUp(600851475143)
	print(res)

def FindLargestPrimeNumberUp(n):
	for i in range(2, int(n/2)):
		if n % i == 0:
			if isPrime(i):
				print(i)

def FindLargestPrimeNumber(n):
	i = (n-1)/2
	while i > 1:
		i = i / 2
		print(i)
		if n % i == 0:
			print(i)
			if isPrime(i):
				return i

def isPrime(n):
    i = n-1
    while i > 1:
        if n % i == 0:
            return False
        i = i - 1
    return True
		

if __name__ == "__main__":
	LargestPrimeFactor()
