# projecteuler.net/problem=5

def main():
    answer = SmallestMultiple()
    print(answer)

def SmallestMultiple():
    num = 1
    while True:
        found = True
        for i in range(1, 20):
            if num % i != 0:
                found = False
                break
        if found:
            return num
        num = num + 1

if __name__ == '__main__':
    main()
