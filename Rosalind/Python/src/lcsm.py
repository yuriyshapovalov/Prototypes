# rosalind.info/problems/lscm

class DNA_string:
    def __init__(self, name, string):
        self.name = name
        self.string = string

def main():
    dna_fasta = []
    data = [line.strip() for line in open('fasta.txt', 'r')]
    
    file_name = ''
    string = ''
    for i in data:
        if len(i) == 0 or i[0] == '>':
            if file_name != '':
                dna_str = DNA_string(file_name, string)
                dna_fasta.append(dna_str)
                file_name = ''
                string = ''
            file_name = i[1:]
        else:
            string += i

    shortest_dna_index = 0
    for i in range(1, len(dna_fasta)):
        if len(dna_fasta[i].string) < len(dna_fasta[shortest_dna_index].string):
            shortest_dna_index = i
    
    i, j = 0, len(dna_fasta[shortest_dna_index].string)
    common_seq = []

    while i < len(dna_fasta[shortest_dna_index].string):
        j = len(dna_fasta[shortest_dna_index].string)
        while j > i+1:
            success = True
            for dna in dna_fasta:
                if dna_fasta[shortest_dna_index].string[i:j] not in dna.string:
                    success = False
                    break
            if success:
                common_seq.append(dna_fasta[shortest_dna_index].string[i:j])
            j -= 1

        i += 1
    longest = ''
    for i in common_seq:
        if len(i) > len(longest):
            longest = i

    print(longest)
if __name__ == '__main__':
    main()
