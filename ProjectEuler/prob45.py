# projecteuler.net/problem=45

def main():
    answer = TPHNumber()
    print("Answer: {}".format(answer))

def TPHNumber():
    triangle = GetTriangleSeq(100000)
    pentagonal = GetPentagonalSeq(100000)
    hexagonal = GetHexagoalSeq(100000)

    c1 = [val for val in triangle if val in pentagonal]
    c2 = [val for val in c1 if val in hexagonal]

    print(c2)

def GetTriangleSeq(n):
    arr = []
    for i in range(1, n):
        t = int((pow(i,2) + i) / 2)
        arr.append(t)
    return arr

def GetPentagonalSeq(n):
    arr = []
    for i in range(1, n):
        t = int((3 * pow(i, 2) - i) / 2)
        arr.append(t)
    return arr

def GetHexagoalSeq(n):
    arr = []
    for i in range(1, n):
        t = 2 * pow(i, 2) - i
        arr.append(t)
    return arr

if __name__ == '__main__':
    main()
