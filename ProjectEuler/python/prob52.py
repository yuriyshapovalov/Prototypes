# projecteuler.net/problem=52

def main():
    answer = PermutatedMul()
    print("Answer: {}".format(answer))

def PermutatedMul():
    i = 1
    muls = [2,3,4,5,6]
    while True:
        found = True
        i += 1
        si = list(str(i))

        ops = list(map(lambda x: x * i, muls))

        for num in ops:
            if len(str(i)) != len(str(num)):
                found = False
                break

        if not found:
            continue

        #print("{} = {}".format(si, ops))

        for num in ops:
            snew = si[:]
            for s in list(str(num)):
                if s in snew:
                    snew.remove(s)
                else:
                    found = False
                    break
                
            if not found:
                break;

        if found:
            break
    return i


if __name__ == '__main__':
    main()
