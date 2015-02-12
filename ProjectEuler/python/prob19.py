# projecteuler.net/problem=19

days = ('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat')
month = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
d_mon = ( 31,    28,    31,    30,    31,    30,    31,    31,    30,    31,    30,    31)
d_mon_leap = ( 31,    29,    31,    30,    31,    30,    31,    31,    30,    31,    30,    31)
start_year = 1900
count_year = 1901
days_in_year = 365

# 01.01.1901 - Tuesday

def main():
    answer = CountingSundays()
    print(answer)

def CountingSundays():
    counter = 0
    daily_iter = 1 # for starting year 01.01.1901 - Tuesday
    for yr in range(1901, 2001):
        m = ()
        if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
            m = d_mon_leap
        else:
            m = d_mon

        i = 0
        for mh in month:
            for ds in range(1, m[i]+1):
                daily_iter += 1
                if daily_iter >= 7:
                    daily_iter = 0
                
                if daily_iter == 0 and ds == 1:
                    counter += 1
                #print("{0}.{1}.{2}: {3}".format(ds, mh, yr, days[daily_iter]))
            i += 1

    return(counter)

if __name__ == '__main__':
    main()
