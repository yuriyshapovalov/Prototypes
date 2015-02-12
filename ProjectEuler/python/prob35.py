# projecteuler.net/problem=35
from itertools import permutations

def main():
	answer = CircularPrime()
	print("\nAnswer: {0}".format(answer))

def CircularPrime():
	count = 0
	for i in range(2, 1000000):
		# because such numbed cannot contain numbers 0, 5, 2, 4, 6, 8
		s = str(i)
		if len(s) > 2:
			if '0' in s or '2' in s or '4' in s or '5' in s or '6' in s or '8' in s:
				continue
		if isPrime(i):
			if CheckPermutationsPrimarity(i):
				count += 1
				print("({0}): {1}".format(count, i))				
	return count

def isPrime(num):
	i = 2
	stop = int(num/2)+1
	while i < stop:
		if num % i == 0:
			return False
		i += 1
	return True

def CheckPermutationsPrimarity(n):
	s = str(n)
	ln = len(s)
	lst = []
	for i in s:
		t = s[0]
		s = s[1:]
		s += t
		lst.append(s)
	#print("({0}) = {1}".format(n, lst))
	# rotations instead of permutations
	# prm = list(permutations(lst))
	for i in lst:
		rnum = ''
		for j in i:
			rnum += j
		if not isPrime(int(rnum)):
			return False
	return True




if __name__ == '__main__':
	main()
