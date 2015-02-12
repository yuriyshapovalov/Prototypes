# projecteuler.net/problem=36

def main():
    answer = DoubleBasePalindromes()
    print(answer)

def DoubleBasePalindromes():
    sum = 0
    for i in range(1, 1000000):
        if isDecPalindrome(i) and isBinPalindrome(i):
            sum += i
    return sum

def isDecPalindrome(n):
    decimal_str = str(n)
    i, j = 0, len(decimal_str)-1
    while i < j:
        if decimal_str[i] != decimal_str[j]:
            return False
        i += 1
        j -= 1
    return True

def isBinPalindrome(n):
    binary_str = bin(n)[2:]
    i, j = 0, len(binary_str)-1
    while i < j:
        if int(binary_str[i]) != int(binary_str[j]):
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    main()
