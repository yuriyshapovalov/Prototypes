# Frequent Words Problem: Find the most frequent k-mers in a string.
import sys

def main(string, k):
    seq = {}
    highest = 0

    for i in range(0, len(string)-k):
        dna_sub = string[i:i+k]
        if dna_sub in seq:
            seq[dna_sub] += 1
            if highest < seq[dna_sub]:
                highest = seq[dna_sub]
        else:
            seq[dna_sub] = 1

    res = ''
    for dna in seq:
        if seq[dna] == highest:
            res = dna + ' ' + res
    print(res)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
