# projecteuler.net/problem=34
from math import factorial

def main():
	answer = DigitFactorials()
	print("Answer: {0}".format(answer))

def DigitFactorials():
	res = 0
	for i in range(3, 100000):
		s = str(i)
		ls = 0
		for j in s:
			ls += factorial(int(j))

		if i == ls:
			res+=i
			print(i)
	return res

if __name__ == '__main__':
	main()
