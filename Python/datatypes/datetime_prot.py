# datetime - basic date and time types
import datetime

def main():
    print("Date object")

    x = datetime.date(2012, 11, 4)
    print("datetime.date(2012, 11, 4) = {}".format(x))

    x = datetime.date.today()
    print("datetime.date.today() = {}".format(x))

    x = datetime.date.fromtimestamp(1234956789)
    print("datetime.date.fromtimestamp(1234956789) = {}".format(x))

    x = datetime.date.fromordinal(1111211)
    print("datetime.date.fromordinal(1111211) = {}".format(x))

    x = datetime.date.max
    print("datetime.date.max = {}".format(x))

    x = datetime.date.min
    print("datetime.date.min = {}".format(x))

    x = datetime.date.resolution
    print("datetime.date.resolution = {}".format(x))

    x = datetime.date.year
    print("datetime.date.year = {}".format(x))

    x = datetime.date.month
    print("datetime.date.month = {}".format(x))

    x = datetime.date.day
    print("datetime.date.day = {}".format(x))

if __name__ == '__main__':
    main()
