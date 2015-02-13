# Calculating Expected Offspring
# http://rosalind.info/problems/iev/
import sys

class iev:

	def main(self, couples):
		pairs = couples.split(" ")
		AAAA = int(pairs[0])
		AAAa = int(pairs[1])
		AAaa = int(pairs[2])
		AaAa = int(pairs[3])
		Aaaa = int(pairs[4])
		aaaa = int(pairs[5])

		return (AAAA * 2) + (AAAa * 2) + (AAaa * 2) + (AaAa * 1.5) + (Aaaa * 1)


if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        raise Exception('ERROR: File name should not be empty!')

    with open(filename, 'r') as seq_file:
        result = iev().main(seq_file.read())
        print(result)