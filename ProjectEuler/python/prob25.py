#projecteuler.net/problem=25

def main():
    answer = FibNumber()
    print(answer)

def FibNumber():
    i = 0
    a,b = 0,1
    while True:
        i += 1
        a,b = b,a+b
        if len(str(a)) >= 1000:
            break
    return i

if __name__ == '__main__':
    main()
