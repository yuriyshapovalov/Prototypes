# rosalind.info/problems/dna
import sys

def main(dna_seq):
    if dna_seq == '':
        return
    
    s = {}
    for i in dna_seq:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1

    print("{} {} {} {}".format(s['A'], s['C'], s['G'], s['T']))

if __name__ == '__main__':
    main(sys.argv[1])
