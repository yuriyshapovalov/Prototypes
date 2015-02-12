# Transcribing DNA into RNA
# rosalind.info/problems/rna
import sys

class rna:
	def main(self, dna_seq):
	    dna_seq = list(dna_seq)

	    for idx, i in enumerate(dna_seq):
	        if i == 'T':
	            dna_seq[idx] = 'U'
	            
	    print(''.join(dna_seq))

if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        rna().main(seq_file.read())
