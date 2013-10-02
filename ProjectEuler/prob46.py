# projecteuler.net/problem=46
from math import sqrt

def main():
    answer = GoldbachConj()
    print("Answer: {}".format(answer))

def GoldbachConj():
    primes = GetPrimeList()

    result = 1
    notFound = True

    while notFound:
        result += 2
        j = 0
        notFound = False
        while result >= primes[j]:
            if isTwiceSquare(result - primes[j]):
                notFound = True
                break
            j += 1
    return result

def isTwiceSquare(n):
    sq = sqrt(n/2)
    return sq == int(sq)

        
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
