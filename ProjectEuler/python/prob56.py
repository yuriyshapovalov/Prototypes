# projecteuler.net/problem=56

def main():
    answer = pow_dig_sum()
    print("Answer: {}".format(answer))

def pow_dig_sum():
    res = 0
    for i in range(1, 101):
        for j in range(1, 101):
            num = i**j

            lst = list(str(num))

            sm = 0
            for k in lst:
                sm += int(k)

            if res < sm:
                res = sm
    return res

if __name__ == '__main__':
    main()
