# rosalind.info/problems/prtm
import sys

def main(amino):
    res = 0
    for i in amino:
        if i == 'A': res += 71.03711
        elif i == 'C': res += 103.00919
        elif i == 'D': res += 115.02694
        elif i == 'E': res += 129.04259
        elif i == 'F': res += 147.06841
        elif i == 'G': res += 57.02146
        elif i == 'H': res += 137.05891
        elif i == 'I': res += 113.08406
        elif i == 'K': res += 128.09496
        elif i == 'L': res += 113.08406
        elif i == 'M': res += 131.04049
        elif i == 'N': res += 114.04293
        elif i == 'P': res += 97.05276
        elif i == 'Q': res += 128.05858
        elif i == 'R': res += 156.10111
        elif i == 'S': res += 87.03203
        elif i == 'T': res += 101.04768
        elif i == 'V': res += 99.06841
        elif i == 'W': res += 186.07931
        elif i == 'Y': res += 163.06333 
 
    print(res)
 
    

if __name__ == '__main__':
    main(sys.argv[1])
