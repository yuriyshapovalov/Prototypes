# projecteuler.net/problem=44

def main():
    answer = PentagonNum()
    #print("Answer: {}".format(answer))

def PentagonNum():
    pennum = []
    for i in range(1, 10000):
        n = int(((3 * (i * i)) - i) / 2)
        pennum.append(n)
    
    for i in pennum:
        for j in pennum:
            sm = i + j
            dif = i - j
            if sm in pennum and dif in pennum:
                print("pair = {} {}: D {}".format(i, j, abs(i - j)))

    return 0

if __name__ == '__main__':
    main()
