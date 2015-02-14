# Consensus and Profile
# rosalind.info/problems/cons/
import sys

class cons:
    def main(self, dna_file):
        if not dna_file:
            raise Exception('ERROR: File is empty.')
        
        data = [line.strip() for line in dna_file]

        matrix = []
        for line in data:
            if str(line[0]) == '>':
                pass
            else:
                matrix.append(list(line))
        matrix = [list(x) for x in zip(*matrix)]

        consensus = ''
        profile = []
        
        for i in matrix:
            profile_dict = {'A' : 0, 'C': 0, 'G': 0, 'T': 0}
            for j in i:
                profile_dict[j] += 1
            profile.append(profile_dict)

        for i in profile:
            counter = 0
            letter = ''
            for j in i:
                if i[j] > counter:
                    counter = i[j]
                    letter = j
            consensus += letter

        print(consensus)

        strA = ''
        strC = ''
        strG = ''
        strT = ''

        for i in profile:
            strA += ''.join(str(i['A'])) + ' '
            strC += ''.join(str(i['C'])) + ' '
            strG += ''.join(str(i['G'])) + ' '
            strT += ''.join(str(i['T'])) + ' '

        print('A: {}'.format(strA))
        print('C: {}'.format(strC))
        print('G: {}'.format(strG))
        print('T: {}'.format(strT))

       

if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        cons().main(seq_file)