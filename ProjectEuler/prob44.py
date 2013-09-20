# projecteuler.net/problem=44

def main():
    answer = PentagonNum()
    print("Answer: {}".format(answer))

def PentagonNum():
    pennum = []
    for i in range(1, 10000):
        n = int(((3 * (i * i)) - i) / 2)
        pennum.append(n)
    
    for i in 

    return pennum

if __name__ == '__main__':
    main()
