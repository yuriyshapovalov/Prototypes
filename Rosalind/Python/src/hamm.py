# rosalind.info/problems/hamm
import sys

def main(s, t):
    counter = 0
    for i in range(0, len(s)-1):
        if s[i] != t[i]:
            counter += 1
    print("result: {}".format(counter))



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
