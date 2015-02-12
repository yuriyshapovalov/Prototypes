# projecteuler.net/problem=24

def main():
    answer = LexPermutation('0123456789', 1000000)
    print("Answer: {}".format(answer))

def LexPermutation(n, numPerm):
    strlist = list(n)
    counter = 1
    while counter < numPerm:
        strlist = Permutate(strlist)
        counter += 1
    res = ''
    for i in strlist:
        res += str(i)
    return res

def Permutate(n):
    length = len(n)
    tail = []
    i = length-1

    while n[i] <= n[i-1]:
        i = i - 1
    
    j = length
    while (n[j-1] <= n[i-1]):
        j = j - 1


    tmp = n[i-1]
    n[i-1] = n[j-1]
    n[j-1] = tmp            

    i += 1
    j = length
    while(i < j):
        tmp = n[i-1]
        n[i-1] = n[j-1]
        n[j-1] = tmp
        i += 1
        j -= 1
    return n


if __name__ == '__main__':
    main()
