#projecteuler.net/problem=43

def main():
    answer = SubStringDivisibility()
    print("Answer: {}".format(answer))

def SubStringDivisibility():
    res = 0
    for num in range(1023456789, 9876543211):
        if Pandigit(num):
            #print("- {}".format(num))
            if SubStringDiv(num):
                res += num
                print("################## {0} --- (1)".format(num, res))
        num -= 1
    return res

def Pandigit(n):
    s = str(n)

    if '0' not in s:
        return False
    if '1' not in s:
        return False
    if '2' not in s:
        return False
    if '3' not in s:
        return False
    if '4' not in s:
        return False
    if '5' not in s:
        return False
    if '6' not in s:
        return False
    if '7' not in s:
        return False
    if '8' not in s:
        return False
    if '9' not in s:
        return False

    return True

def SubStringDiv(n):
    s = str(n)

    if int(s[1:4]) % 2 != 0:
        return False
    if int(s[2:5]) % 3 != 0:
        return False
    if int(s[3:6]) % 5 != 0:
        return False
    if int(s[4:7]) % 7 != 0:
        return False
    if int(s[5:8]) % 11 != 0:
        return False
    if int(s[6:9]) % 13 != 0:
        return False
    if int(s[7:10]) % 17 != 0:
        return False

    return True

if __name__ == '__main__':
    main()
