# projecteuler.net/problem=40

def main():
    answer = ChampConst()
    print("Answer: {}".format(answer))

def ChampConst():
    s = ''
    i = 1
    while len(s) < 1000010:
        s += str(i)
        i += 1
    return int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

if __name__ == '__main__':
    main()
