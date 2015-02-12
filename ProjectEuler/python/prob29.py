# projecteuler.net/problem=29

def main():
	answer = DistinctPowers(100)
	print(len(answer))

def DistinctPowers(n):
	powers = set()
	for i in range(2, n+1):
		for j in range(2, n+1):
			num = pow(i,j)
			if num not in powers:
				powers.add(num)
	return sorted(powers)

if __name__ == '__main__':
	main()
