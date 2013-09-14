# rosalind.info/problems/ini3
import sys

def main(s, a, b, c, d):
    if s == '':
        return
    
    a = int(a) if a != '' else 0
    b = int(b) if b != '' else 0
    c = int(c) if c != '' else 0
    d = int(d) if d != '' else 0
    
    if len(s) < max(a,b,c,d):
        return

    print(s[a:b+1] + ' ' + s[c:d+1])

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
