# Pattern Matching Problem: Find all occurrences of a pattern in a string.
import sys

def main(pattern):
    dna = ''
    with open('dna.txt', 'r') as f:
        dna = f.read()
    res = ''
    ln = len(pattern)
    for i in range(0, len(dna)):
        if dna[i: i+ln] == pattern:
            res += str(i) + ' '
    print(res)

if __name__ == '__main__':
    main(sys.argv[1])
