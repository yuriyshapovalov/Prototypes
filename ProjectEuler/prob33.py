# projecteuler.net/problem=33

def main():
    answer = CancellingFractions()
    print("Answer: {}".format(answer))

def CancellingFractions():
    prod = 1.0
    for i in range(10, 100):
        for j in range(i+1, 100):
            n = i/j
            #print("{}/{} = {}".format(j,i,n))

            il = list(str(i))
            jl = list(str(j))

            if i % 10 != 0:
                #print("{} / {}".format(il, jl))
                for k in il:
                    if k in jl:            
                        il.remove(k)
                        jl.remove(k)

                        ii = int(il[0])
                        jj = int(jl[0])

                        if jj != 0 and ii/jj == n:
                            prod *= ii/jj
                            #print("\n{}/{} = {}".format(i,j,n))
                            #print("== {}/{} = {}".format(ii,jj,ii/jj))
                            #print(prod)


    return prod        

            

if __name__ == '__main__':
    main()
