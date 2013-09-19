# projecteuler.net/problem=24

def main():
    answer = LexPermutation('0123', 1000000)
    print(answer)

def LexPermutation(n, numPerm):
    strlist = list(n)
    counter = 1
    while counter < numPerm:
        res = Permutate(strlist)
        #print(res)
        counter += 1

def Permutate(n):
    print(n)
    length = len(n)
    tail = []

    i = length-1
    while i > 0:
        if n[i] > n[i-1]:

            tmp = n[i]
            n[i] = n[i-1]
            n[i-1] = tmp            

            if len(tail) > 0:
                #print("tail not empty")

                tk = 0
                k = i+1
                while tk < len(tail):
                    #print("{0} | {1} ({2})|({3})".format(n, tail, k, tk))
                    n[k] = tail[tk]
                    k += 1
                    tk += 1
                tail.clear()
            return n
            #print('trace {0} - {1}'.format(n[i], n[i-1]))

        else:
            tail.append(n[i])
        i -= 1

if __name__ == '__main__':
    main()
