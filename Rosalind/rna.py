# rosalind.info/problems/rna
import sys

def main(dna):
    dna_seq = list(dna)

    for idx, i in enumerate(dna_seq):
        if i == 'T':
            dna_seq[idx] = 'U'
    print(''.join(dna_seq))

if __name__ == '__main__':
    main(sys.argv[1])
