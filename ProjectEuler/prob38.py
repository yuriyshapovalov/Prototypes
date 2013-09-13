# projecteuler.net/problem=38

def main():
    answer = PandigitMul()
    print("Answer: {0}".format(answer))

def PandigitMul():
    hPan = 0
    for i in range(1, 10000):
        sm = ''
        for j in range(1, 9):
            sm += str(i * j)
            if len(sm) > 9:
                break
            smi = int(sm)

            if isPandigit(smi):
                if smi > hPan:
                    hPan = smi
                    print("{0}x{1} = {2}".format(i, j, sm))
    return hPan

def isPandigit(n):
    s = str(n)
    if '1' not in s or '2' not in s or '3' not in s or '4' not in s or '5' not in s or '6' not in s or '7' not in s or '8' not in s or '9' not in s:
        return False
    return True

if __name__ == '__main__':
    main()
