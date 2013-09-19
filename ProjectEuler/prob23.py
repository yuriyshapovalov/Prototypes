# projecteuler.net/problem=23
from math import sqrt

def main():
    answer = NonAbundantSums()
    print("Answer: {}".format(answer))

def NonAbundantSums():
    abund_nums = []
    arr = [x for x in range(1, 28123)]
    for i in range(12, 28124):
        sm = SumOfAllDivisors(i)
        if sm > i:
            #print("{} = {}".format(i, sm))
            abund_nums.append(i)

    print(len(abund_nums))
    
    deq_sq = set()
    ln = len(abund_nums)-1
    pos = 0
    for i in range(0, ln):
        for j in range(pos, ln):
            prd = i + j
            deq_sq.add(prd)
            if prd in arr:
                arr.remove(prd)
        pos += 1

    print(len(deq_sq))

    sm = 0
    for i in arr:
        sm += i
    return sm

    

def SumOfAllDivisors(n):
    nod = 0
    sq = int(n/2)+1
    i = 1
    while i <= sq:
        if n % i == 0:
            nod += i
        i += 1

    return nod

if __name__ == '__main__':
    main()
