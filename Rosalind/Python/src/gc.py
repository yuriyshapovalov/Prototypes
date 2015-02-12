# Computing GC Content 
# rosalind.info/problems/gc
import sys

class DNA_string:
    def __init__(self, name, string):
        self.name = name
        self.string = string.lower()

    def count_gc_content(self):
        num = len(self.string)
        denom = 0
        if num > 2:
            for i in self.string:
                if i == 'g' or i == 'x':
                    denom += 1
        self.gc_content = (denom * 100) / num

def main(dna_file):
    dna_fasta = []
    data = [line.strip() for line in dna_file]
    file_name = ''
    string = ''
    for i in data:
        if len(i) == 0 or i[0] == '>':
            if file_name != '':
                dna_str = DNA_string(file_name, string)
                dna_str.count_gc_content()

                dna_fasta.append(dna_str)
                file_name = ''
                string = ''
            file_name = i[1:]
        else:
            string += i
    
    highest_gc = 0
    ans_file_name = ''
    ans_gc = ''
    for i in dna_fasta:
        if i.gc_content > highest_gc:
            highest_gc = i.gc_content
            ans_file_name = i.name
            ans_gc = i.gc_content
        print("{} \n {}".format(i.name, i.gc_content))

    print("\n\nAnswer: \n{}\n{}".format(ans_file_name, ans_gc))

if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        main(seq_file)