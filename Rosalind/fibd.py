# rosalind.info/problems/fibd
import sys

def main(n, k):
    pair = 0
    childs = 1
    died = []
    print("pair: {} childs: {} \n".format(pair, childs))
    for i in range(1, n):
        died.append(childs)

        sub_child = pair
        pair += childs
        childs = sub_child

        if i >= k:
            print("died: {}".format(died[i-k]))
            pair -= died[i-k]

        
        print("pair: {} childs: {}\n".format(pair, childs))
        
    print (childs + pair)
        

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
