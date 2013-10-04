# Most common used methods

def ESieve(n):
    """ Get list of prime numbers """
    multiples = []
    prime = []
    for i in range(2, n+1):
        if i not in multiples:
            prime.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return prime

def isPrime(num):
    """ Check is number primarity """
	i = 2
	stop = int(num/2)+1
	while i < stop:
		if num % i == 0:
			return False
		i += 1
	return True
