# projecteuler.net/problem=6

def SumSquareDifference():
	sum_of_sq = SumOfSquare(100)
	sq_of_sum = SquareOfSum(100)
	answer = sq_of_sum - sum_of_sq
	print(answer)

def SumOfSquare(n):
	res = 0
	for i in range(1, n+1):
		res = res + i*i
	return res

def SquareOfSum(n):
	res = 0
	for i in range(1, n+1):
		res = res + i
	return res*res

if __name__ == '__main__':
	SumSquareDifference()
