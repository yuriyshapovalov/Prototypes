# projecteuler.net/problem=14

def main():
    answer = LongestCollatzSeq()
    print(answer)

def LongestCollatzSeq():
    highest_num = 0
    res = 0
    for i in range(1, 1000000):
        seq = genCollatz(i)
        if seq > highest_num:
            res = i
            highest_num = seq
    return res
    

def genCollatz(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
            counter += 1
        else:
            counter += 1
            n = int(3 * n + 1)

    return counter

if __name__ == '__main__':
    main()
