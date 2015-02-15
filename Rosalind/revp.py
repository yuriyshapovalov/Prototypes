# Locating Restriction Sites
# rosalind.info/problems/revp/
import sys

class revp:
	def main(self, dna_seq):

		reversed_string = ''
		for i in dna_seq:
			if i == 'A':
				reversed_string += 'T'
			elif i == 'T':
				reversed_string += 'A'
			elif i == 'C':
				reversed_string += 'G'
			elif i == 'G':
				reversed_string += 'C'

	#	print(dna_seq)
	#	print(reversed_string)


		for i in range(0, len(dna_seq)-4):
			j = 4
			while (j <= 12):
				if (i + j > len(dna_seq)):
					j+=1
					continue
				if self.isPalindrome(dna_seq[i:i+j], reversed_string[i:i+j]):
					rs = reversed_string[i:i+j]
					#print("{} {} - {} = {}".format(i+1, j, dna_seq[i:i+j], rs[::-1]))
					print("{} {}".format(i+1, j))
				j+=1
			i+=1

	def isPalindrome(self, string, reversed_string):
		return string == reversed_string[::-1]

if __name__ == '__main__':
	filename = sys.argv[1]
	if not filename:
		raise Exception('ERROR: File name should not be empty!')

	with open(filename, 'r') as dna_file:
		data = [line.strip() for line in dna_file]
		string = ''
		for i in data:
			if len(i) != 0 and i[0] != '>':
				string += i
        revp().main(string)