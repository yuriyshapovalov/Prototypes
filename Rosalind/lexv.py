# Ordering Strings of Varying Length Lexicographically
# rosalind.info/problems/lexv/
import sys
from itertools import *

class lexv:
    def combine(self, symbols, n, vary='', result=[]):
        if n > 0:
            for sym in symbols:
                el = vary + sym
                result.append(el)
                self.combine(symbols, n - 1, el, result)

        return result

    def main(self, dna_file):
        symbols = dna_file.readline()
        symbols = list(symbols[:-1])
        symbols = filter(lambda x: str(x) != ' ' , symbols)
        n = int(dna_file.readline())

        return self.combine(symbols, n)

if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        result = lexv().main(seq_file)
        print('\n'.join(result))