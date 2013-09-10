# projecteuler.net/problem=21

def main():
	answer = AmicableNumbers(10000)
	print(answer)

def AmicableNumbers(n):
	sum = 0
	for i in range(1, n):
		ami = 0
		div = GetDivisorsSum(i)
		ami_div = GetDivisorsSum(div)

		if ami_div == i:
			if i != div:
				print("{}: ({}) {} ".format(i, ami, div))
				sum += i

		
	return sum

def GetDivisorsList(n):
	divisors = []
	divisors.append(1)
	i = int(n/2)
	while i > 1:
		if n % i == 0:
			divisors.append(i)
		i -= 1
	return divisors

def GetDivisorsSum(n):
	div_sum = 0
	lst = GetDivisorsList(n)
	for j in lst:
		div_sum += j
	return div_sum

if __name__ == '__main__':
	main()
