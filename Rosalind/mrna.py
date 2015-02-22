# Inferring mRNA from Protein
# rosalind.info/problems/mrna/
import sys

class mrna:
    codon_freq = {'F':2, 'L':6, 'S':6, 'Y':2, 'A':4, 'C':2, 
                  'W':1, 'P':4, 'H':2, 'Q':2, 'R':6, 'I':3,
                  'M':1, 'N':2, 'K':2, 'D':2, 'V':4, 'E':2,
                  'G':4, 'T':4, 'stop':3}

    def main(self, dna_seq):
        if not dna_seq:
            raise Exception('ERROR: File is empty.')
        
        res = self.codon_freq['stop']
        for i in range(len(dna_seq)):
            res *= self.codon_freq[dna_seq[i]]

        return res % 1000000

if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        result = mrna().main(seq_file.read())
        print(result)