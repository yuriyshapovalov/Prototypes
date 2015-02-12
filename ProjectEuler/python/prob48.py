# projecteuler.net/problem=48

def main():
    answer = SelfPowerSum(1000)
    print(answer)

def SelfPowerSum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + pow(i, i)
    return sum

if __name__ == '__main__':
    main()
