# projecteuler.net/problem=55

def main():
    answer = LychrelNum()
    print("Answer: {}".format(answer))

def LychrelNum():
    res = 0
    for i in range(10, 10001):
        counter = 50
        num = i
        is_lychrel = True

        while counter > 0:

            rev_num = int(str(num)[::-1])
            l_num = str(num + rev_num)

            if is_palindrom(l_num):
                is_lychrel = False
                break

            counter -= 1
            num = int(l_num)

        if is_lychrel:
            res += 1
            print("({}): {}".format(res, i))

    return res

def is_palindrom(num):
    st_num = str(num)
    i, j = 0, len(st_num)-1
    while i < j:
        if st_num[i] != st_num[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    main()
