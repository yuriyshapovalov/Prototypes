# projecteuler.net/problem=24

def main():
    answer = LexPermutation('012')
    print(answer)

def LexPermutation(n):
    strlist = []
    for i in n:
        strlist.append(i)
    print(strlist)
    res = n
    counter = 0
    while counter < 5:
        res = Permutate(strlist)
        print(res)
        counter += 1

def Permutate(n):
    length = len(n)
    tail = []

    i = length-1
    while i > 0:
        if n[i] > n[i-1]:
            if len(tail) > 0:
                print("tail not empty")
                tail = tail[::-1]
                for j in range(i, len(tail)):
                    n[j] = tail[j-i]

            print('trace {0} - {1}'.format(n[i], n[i-1]))
            tmp = n[i]
            n[i] = n[i-1]
            n[i-1] = tmp

            
            return n
        else:
            tail.append(n[i])
        i -= 1

if __name__ == '__main__':
    main()
