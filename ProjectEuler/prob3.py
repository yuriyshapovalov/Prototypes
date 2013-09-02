# projecteuler.net/problem=3

def LargestPrimeFactor():
	res = FindLargestPrimeNumber(600851475143)
	print(res)

def FindLargestPrimeNumber(n):
	i = n
	while i > 1:
		i = i - 1
		if n % i == 0:
			j = i
			prime = True
			while j > 2:
				j = j - 1
				if i % j == 0:
					prime = False
					break
			if prime:
				return i


		

if __name__ == "__main__":
	LargestPrimeFactor()
