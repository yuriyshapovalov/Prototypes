# Complementing a Strand of DNA 
# rosalind.info/problems/revc
import sys

class revc:
    def main(self, dna_seq):
        res = ''
        seq = list(dna_seq[::-1])
        for x, i in enumerate(seq):
            if i == 'A':
                seq[x] = 'T'
            elif i == 'T':
                seq[x] = 'A'
            elif i == 'C':
                seq[x] = 'G'
            elif i == 'G':
                seq[x] = 'C'

        print(''.join(seq))


if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        revc().main(seq_file.read())
