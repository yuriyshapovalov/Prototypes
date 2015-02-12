# projecteuler.net/problem=32

def main():
    answer = PandigitProduct()
    print("Answer: {0}".format(answer))

def PandigitProduct():
    prodRes = 0
    nums = set()

    for i in range(1, 10000):
        for j in range (i, 10000):

            prod = i*j
            sProd = str(i) + str(j) + str(prod)

            if len(sProd) < 9:
                continue

            if len(sProd) > 9:
                break

            if isPandigit(sProd):
                nums.add(prod)
                
    for i in nums:
        prodRes += i

    return prodRes

def isPandigit(s):
    l = len(s)+1
    pandigit = True

    for i in range(1, l):
        if str(i) not in s:
            pandigit = False
    return pandigit

if __name__ == '__main__':
    main()
