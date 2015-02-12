# projecteuler.net/problem=50

def main():
    answer = ConsPrimes()
    print("Answer".format(answer))

def ConsPrimes():
    primes = GetPrimeList()
    res = 0
    counts = 0
    i, j = 0,2

    while i < j:
        
        num = primes[i:j]

        if sum(num) < 1000:
            j += 1
            continue

        # manage slice of primes
        if sum(num) > 1000000:
            i += 1
            while sum(primes[i:j]) > 1000:
                    j -= 1

        num = sum(primes[i:j])

        if isPrime(num):
            if counts < j-i:
                counts = j-i;
                res = num
                print("({}) = {}".format(counts, res))

        j += 1
    return res

def GetPrimeList():
    primes = []
    for i in range(2, 10000):
        if isPrime(i):
            primes.append(i)
    return primes

def isPrime(num):
	i = 2
	stop = int(num/2)+1
	while i < stop:
		if num % i == 0:
			return False
		i += 1
	return True

if __name__ == '__main__':
    main()
