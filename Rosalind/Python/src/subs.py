# rosalind.info/problems/subs
import sys

def main(sub_dna):
    occured = ''
    dna = ''
    with open('dna.txt', 'r') as dna_file:
        dna = dna_file.read()
    sub_dna_len = len(sub_dna)
    i_stop = (len(dna) - 1) - sub_dna_len
    for i in range(0, i_stop):
        if dna[i:i+sub_dna_len] == sub_dna:
            occured += str(i+1) + ' '
    print(occured)

if __name__ == '__main__':
    main(str(sys.argv[1]))
