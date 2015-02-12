# projecteuler.net/problem=28

def main():
	answer = DiagonalSumMatrix(1001)
	print(answer)

def DiagonalSumMatrix(n):
	summ = 0
	i = 1
	iterations = (n*n)+1
	sqr = 4
	inc = 2
	while i < iterations:
		summ += i
		if sqr == 0:
			inc += 2
			sqr = 4

		i += inc
		sqr -= 1
	
	return summ

if __name__ == '__main__':
	main()
