# projecteuler.net/problem=41

def main():
    answer = PandigitalPrime()
    print("Answer: {}".format(answer))

def PandigitalPrime():
    num = 987654321

    while num > 1:
        if Pandigit(num):
            print("- {}".format(num))
            if Prime(num):
                return num
        num -= 1

def Pandigit(n):
    s = str(n)
    l = len(s)+1
    for i in range(1, l):
        if str(i) not in s:
            return False
    return True

def Prime(n):
    to = int(n/2)+1
    for i in range(2, to):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
