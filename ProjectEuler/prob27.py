# projecteuler.net/problem=27

def main():
    answer = QuadraticPrimes()
    print("Answer: {}".format(answer))

def QuadraticPrimes():
    a, b = 1,1
    highest = 1
    
    for i in range(1, 1000):
        for j in range(1, 1000):
            
            k = 0
            while True:
                res = (pow(k, 2) + i * k) + j

                if isPrime(res):
                    k += 1
                else:
                    break

            if k > highest:
                print("({}): a = {} b = {}".format(k, a, b))
                highest = k
                a = i
                b = j

        #print(i)
    return a*b

def isPrime(n):
    to = int(n/2) -1
    for i in range(2, to):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
