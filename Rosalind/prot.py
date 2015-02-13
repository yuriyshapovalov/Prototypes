# Translating RNA into Protein
# rosalind.info/problems/prot

def main():
    protein = ''
    with open('mrna.txt', 'r') as mrna:
        mrna_str = mrna.read()
        
        i = 0
        while i < len(mrna_str) - 3:
            prt = mrna_str[i:i+3]
            
            if prt == 'UUU' or prt == 'UUC':
                protein += 'F'
            elif prt == 'UUA' or prt == 'UUG' or prt == 'CUU' or prt == 'CUC' or prt == 'CUA' or prt == 'CUG':
                protein += 'L'
            elif prt == 'UCU' or prt == 'UCC' or prt == 'UCA' or prt == 'UCG':
                protein += 'S'
            elif prt == 'UAU' or prt == 'UAC':
                protein += 'Y'
            elif prt == 'UGU' or prt == 'UGC':
                protein += 'C'
            elif prt == 'UGG':
                protein += 'W'
            elif prt == 'CCU' or prt == 'CCC' or prt == 'CCA' or prt == 'CCG':
                protein += 'P'
            elif prt == 'CAU' or prt == 'CAC':
                protein += 'H'
            elif prt == 'CAA' or prt == 'CAG':
                protein += 'Q'
            elif prt == 'CGU' or prt == 'CGC' or prt == 'CGA' or prt == 'CGG':
                protein += 'R'
            elif prt == 'AUU' or prt == 'AUC' or prt == 'AUA':
                protein += 'I'
            elif prt == 'AUG':
                protein += 'M'
            elif prt == 'ACU' or prt == 'ACC' or prt == 'ACA' or prt == 'ACG':
                protein += 'T'
            elif prt == 'AAU' or prt == 'AAC':
                protein += 'N'
            elif prt == 'AAA' or prt == 'AAG':
                protein += 'K'
            elif prt == 'AGU' or prt == 'AGC':
                protein += 'S'
            elif prt == 'AGA' or prt == 'AGG':
                protein += 'R'
            elif prt == 'GUU' or prt == 'GUC' or prt == 'GUA' or prt == 'GUG':
                protein += 'V'
            elif prt == 'GCU' or prt == 'GCC' or prt == 'GCA' or prt == 'GCG':
                protein += 'A'
            elif prt == 'GAU' or prt == 'GAC':
                protein += 'D'
            elif prt == 'GAA' or prt == 'GAG':
                protein += 'E'
            elif prt == 'GGU' or prt == 'GGC' or prt == 'GGA' or prt == 'GGG':
                protein += 'G'
            elif prt == 'UAA' or prt == 'UAG' or prt == 'UGA':
                break
            
            i += 3

    print(protein)

if __name__ == '__main__':
    main()
