# Enumerating k-mers Lexicographically
# http://rosalind.info/problems/lexf/
import sys
from itertools import *

class lexf:
	def main(self, dna_file):
		symbols = dna_file.readline()
		symbols = list(symbols[:-1])
		symbols = filter(lambda x: str(x) != ' ' , symbols)
		n = int(dna_file.readline())

		result = list(product(symbols, repeat=n))
		for i in result:
			cout = ''
			for j in i:
				cout += str(j)
			print(cout)


if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        lexf().main(seq_file)