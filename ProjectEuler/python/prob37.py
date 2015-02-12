# projecteuler.net/problem=37

def main():
    answer = TruncPrimes()
    print("Answer: {}".format(answer))

def TruncPrimes():
    sum = 0
    counter = 11
    i = 10
    while counter > 0:
        if isTruncPrime(i):
            sum += i
            print("({0}) - {1}".format(counter, i))
            counter -= 1
        i += 1
    return sum


def isTruncPrime(n):
    s = str(n)
    l = len(s)
    if '4' in s or '6' in s or '8' in s or '0' in s:
        return False

    if not isPrime(n):
        return False

    #print('Prime: {}'.format(n))
# check left truncability
    for t in range(0, l):
        ts = int(s[t:])
        #print('< {0}'.format(ts))
        if not isPrime(ts):
            return False

# check right truncability
    for t in range(1, l):
        ts = int(s[:t])
        #print('> {0}'.format(ts))
        if not isPrime(ts):
            return False

    return True

def isPrime(n):
    if n == 1:
        return False
    sup = int(n/2)+1
    for i in range(2, sup):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
