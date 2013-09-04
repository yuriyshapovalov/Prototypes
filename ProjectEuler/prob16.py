# projecteuler.net/problem=16

def main():
    answer = PowerDigitSum()
    print(answer)

def PowerDigitSum():
    num = str(pow(2, 1000))
    res = 0
    for i in range(0, len(str(num))):
        res += int(num[i])
    return res

if __name__ == '__main__':
    main()
