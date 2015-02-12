# projecteuler.net/problem=63

def main():
    answer = PowerfulDigitCounts()
    print(answer)

def PowerfulDigitCounts():
    count = 0
    for i in range(1, 20):
        for j in range(1, 30):
            res = pow(i, j)

            if len(str(res)) == j:
                count += 1
                print("({0})- {1}~{2}".format(count, i, j))
    return count

if __name__ == '__main__':
    main()
