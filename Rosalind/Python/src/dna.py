# Counting DNA Nucleotides
# rosalind.info/problems/dna
import sys

class dna:
    def main(self, dna_seq):
        if not dna_seq:
            raise Exception('ERROR: File is empty.')
        
        nucleotide = {}
        for i in dna_seq:
            if i in nucleotide:
                nucleotide[i] += 1
            else:
                nucleotide[i] = 1

        adenine = nucleotide['A']
        cytosine = nucleotide['C'] 
        guanine = nucleotide['G']
        thymin = nucleotide['T']
        print("{} {} {} {}".format(adenine, cytosine, guanine, thymin))

        print("\n\n =================================================")
        print("Adenine: {}\nCytosine: {}\nGuanin: {}\nThymine: {}"
            .format(adenine, cytosine, guanine, thymin))
        print("\nAdenine-Thymine: {}\nCytosine-Guanine: {}"
            .format(adenine+thymin, cytosine+guanine))

if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        dna().main(seq_file.read())