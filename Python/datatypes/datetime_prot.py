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

    d = datetime.date(2012, 11, 28)
    x = d.year
    print("({}) datetime.date.year = {}".format(d, x))

    x = d.month
    print("({}) datetime.date.month = {}".format(d, x))

    x = d.day
    print("({}) datetime.date.day = {}".format(d, x))
    
    x = d.replace(year=2013)
    print("({}) datetime.date.replace(year=2013) = {}".format(d, x))

    x = d.timetuple()
    print("({}) datetime.date.timetuple() = {}".format(d, x))

    x = d.toordinal()
    print("({}) datetime.date.toordinal() = {}".format(d, x))

    x = d.weekday()
    print("({}) datetime.date.weekday() = {}".format(d, x))

    x = d.isoweekday()
    print("({}) datetime.date.isoweekday() = {}".format(d, x))

    x = d.isocalendar()
    print("({}) datetime.date.isocalendar() = {}".format(d, x))

    x = d.isoformat()
    print("({}) datetime.date.isoformat() = {}".format(d, x))

    x = d.__str__()
    print("({}) datetime.date.__str__ = {}".format(d, x))

    x = d.ctime()
    print("({}) datetime.date.ctime() = {}".format(d, x))

    x = d.strftime("%d %a %b")
    print("({}) datetime.date.strftime('%d %a %b') = {}".format(d, x))

    x = d.__format__("%A-%B-%w")
    print("({}) datetime.date.__format__() = {}".format(d, x))

    print("\tDatetime object")


if __name__ == '__main__':
    main()
