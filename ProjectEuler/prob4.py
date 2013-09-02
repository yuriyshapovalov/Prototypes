# projecteuler.net/problem=4

def main():
    answer = LargestPalindromeProduct()
    print(answer)

def LargestPalindromeProduct():
    i = 999
    while i > 1:
        j = 999
        while j > 1:
            res = IsPalindromeProduct(i, j)
            if res:
                return i * j
            j = j - 1
        i = i - 1
    print("Answer not found")

def IsPalindromeProduct(x, y):
    prod = str(x * y)
    i = 0
    j = len(prod)-1
    while i < j:
        if prod[i] != prod[j]:
            return False
        i = i + 1
        j = j - 1
    return True

if __name__ == '__main__':
    main()
