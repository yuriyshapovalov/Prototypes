#projecteuler.net/problem=9
from math import *

def main():
	answer = PythagorianTriplet()
	print(answer)
	
def PythagorianTriplet():
	for i in range(1, 1000):
		for j in range(i, 1000):
			x = sqrt(pow(i,2) + pow(j,2))
			if x % 1 == 0:
				res = x + i + j
				if res == 1000:
					return int(x*i*j)

if __name__ == '__main__':
	main()
