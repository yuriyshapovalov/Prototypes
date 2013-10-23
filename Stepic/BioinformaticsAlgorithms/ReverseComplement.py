# Reverse Complement Problem: Reverse complement a nucleotide pattern

def main():
    dna = ''
    with open('dna.txt', 'r') as f:
        dna = f.read()

    comp_dna = ''

    for i in dna[::-1]:
        if i == 'A':
            comp_dna += 'T'
        elif i == 'T':
            comp_dna += 'A'
        elif i == 'C':
            comp_dna += 'G'
        elif i == 'G':
            comp_dna += 'C'

    with open('res.txt', 'w') as f:
        f.write(comp_dna)

    print(comp_dna)

if __name__ == '__main__':
    main()
