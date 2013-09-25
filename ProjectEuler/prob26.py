# projecteuler.net/problem=26

def main():
    answer = ReciprocalCycles()
    print("\nAnswer: {}".format(answer))

def ReciprocalCycles():
    i = 1000
    seqLen = 0

    while i > 1:
        if seqLen >= i:
            break

        remainders = []
        for i in range(0, i):
            remainders.append(0)
        value = 1
        position = 0
        

        while remainders[value] == 0 and value != 0:
            remainders[value] = position
            value *= 10
            value %= i
            position += 1

        if position - remainders[value] > seqLen:
            seqLen = position - remainders[value]

        i -= 1
    return i+1

if __name__ == '__main__':
    main()
