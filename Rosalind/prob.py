# Introduction to Random Strings
# rosalind.info/problems/prob/
import sys
from math import log10

class prob:

    def main(self, dna_file):
        string = dna_file.readline().strip()
        arr = [float(x) for x in dna_file.readline().split(' ')]

        base_AT = string.count('A') + string.count('T')
        base_GC = len(string) - base_AT

        res = []
        for p in range(0, len(arr)):
            x = log10((arr[p]/2)**base_GC * (0.5-arr[p]/2)**base_AT)
            res.append(str(x))
        return res

if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        result = prob().main(seq_file)
        print(' '.join(result))