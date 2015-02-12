# projecteuler.net/problem=17

def main():
    answer = NumberLetterCounts()
    print(answer)

def NumberLetterCounts():
    res = 0
    for i in range(1, 1001):
        res += len(StringifyNumber(i))
        print(StringifyNumber(i))
    
    return res
    

num = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tens = ('twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
uppers = ('hundred', 'thousand', 'million')

    
def StringifyNumber(n):
    string = str(n)
    length = len(string)

    res = ''
    if length > 3:
        index = int(string[0])
        res += num[index] + uppers[1]
        string = string[1:]
    if length > 2:
        index = int(string[0])
        if index != 0:
            res += num[index] + uppers[0]
        string = string[1:]

    if length > 1 and int(string) > 19:
        if int(string[0]) == 0 and int(string[1]) == 0:
            return res
        if len(res) > 0:
            res += 'and'
        if int(string[0]) != 0:
            res += tens[int(string[0])-2]
        if int(string[1]) != 0:
            res += num[int(string[1])]

        string = string[2:]
        return res

    if length > 1 and int(string) <= 19:
        if int(string) == 0:
            return res
        if len(res) > 0:
            res += 'and'
        res += num[int(string)]
        string = string[2:]
        return res
    if length == 1:
        if int(string[0]) != 0:
            if len(res) > 0:
                res += 'and'
            res += num[int(string[0])]

    return res


if __name__ == "__main__":
    main()
