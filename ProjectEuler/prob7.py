# projecteuler.com/problem=7

def main():
	res = NstPrime(10001)
	print(res)
	#for i in range(1, 100):
		#if isPrime(i):
			#print(i)

def NstPrime(n):
	i = 2
	while n >= 1:
		if isPrime(i):
			n = n - 1
		i = i + 1
	
	return i-1

def isPrime(n):
	i = n-1
	while i > 1:
		if n % i == 0:
			return False
		i = i - 1
	return True

if __name__ == '__main__':
	main()
