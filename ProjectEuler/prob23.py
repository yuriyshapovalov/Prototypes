# projecteuler.net/problem=23

def main():
    answer = NonAbundantSums()
    print("Answer: {}".format(answer))

def NonAbundantSums():
    abund_nums = []
    print('Preparing ... ')
    arr = [x for x in range(1, 28123)]
    print('Finding abundant numbers ... ')
    for i in range(1, 28123):
        sm = SumOfAllDivisors(i)
        if sm > i:
            abund_nums.append(i)

    print('Cleaning set of non abundant numbers ... ')
    ab_len = len(abund_nums) - 1
    for i in range(1, ab_len):
        for j in range(i, ab_len):
            s = i + j
            if s in arr:
                arr.remove(s)

    sm = 0
    for i in arr:
        sm += i
    return sm

    

def SumOfAllDivisors(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            sum += i
    return sum

if __name__ == '__main__':
    main()
