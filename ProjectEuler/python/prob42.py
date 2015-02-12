# projecteuler.net/problem=42

def main():
    res = 0
    words = []
    tri_list = []
    with open("words.txt", "r") as f:
        txt = f.read()
        wrd_tmp = txt.split(',')

        for i in wrd_tmp:
            words.append(i[1:-1])

    tri_num = 0
    i = 0
    while i < 1000:
        i += 1
        tri_num += i
        tri_list.append(tri_num)

    for w in words:
        nm = 0
        for c in w:
            nm += ord(c)-64
        
        if nm in tri_list:
            res += 1
            print("({0}){1}".format(nm, w))
    print("\nAnswer: {0}".format(res))


if __name__ == '__main__':
    main()
