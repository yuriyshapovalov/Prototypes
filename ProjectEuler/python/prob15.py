# projecteuler.net/problem=15

def main():
    answer = LatticePaths(20)
    print(answer)

def LatticePaths(x):
    x += 1 # each item represent not cell but line (for close lattice n+1)
    arr = [[0 for i in range(0, x)] for i in range(0, x)]
    arr[0][0] = 1

    for i in range(0, x):
        arr[0][i] = 1
        arr[i][0] = 1

    for diag in range(1, x+1):
        i = diag - 2
        j = 1

        for t in range(0, diag - 2):
            arr[i-t][j+t] = arr[i-t-1][j+t] + arr[i-t][j+t-1]

    j = 1
    for diag in reversed(range(1, x)):
        i = x-1
        for t in range(0, diag):
            arr[i-t][j+t] = arr[i-t-1][j+t] + arr[i-t][j+t-1]
        j += 1

    return arr[x-1][x-1]


if __name__ == '__main__':
    main()
