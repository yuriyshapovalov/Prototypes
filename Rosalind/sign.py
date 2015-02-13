# Enumerating Oriented Gene Orderings
# http://rosalind.info/problems/sign/
import sys
from itertools import *

class sign:
	def combine(self, prod):
	    res = []
	    var, signs = prod
	    for i, num in enumerate(var):
	        sign = signs[i]
	        num = int(sign + str(num))
	        res.append(num)
	    return res


	def main(self, n):
	    variations = list(permutations(range(1, n + 1)))
	    signs = list(product('-+', repeat=n))

	    results = map(self.combine, list(product(variations, signs)))
	    return list(results)

if __name__ == '__main__':
	result = sign().main(int(sys.argv[1]))

	print(len(result))
	for i in result:
		print(' '.join(map(str, i)))