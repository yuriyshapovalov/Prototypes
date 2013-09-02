# projecteuler.net/problem=2
from functools import reduce

def EvenFibonacciSum():
	result = fib(4000000)
	even = filter(lambda x: x % 2 == 0, result);
	sum = reduce(lambda x, y: x + y, even)
	print(sum)

def fib(n):
	seq = []
	a,b = 0, 1
	while True:		
		a, b = b, a + b
		if b >= n:
			break
		seq.append(b)

	return seq

if __name__ == '__main__':
	EvenFibonacciSum()
