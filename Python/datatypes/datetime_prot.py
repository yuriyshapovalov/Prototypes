# datetime - basic date and time types
import datetime

class DatetimeTest:
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

        print("\nDatetime object")

        d = datetime.datetime(2013, 10, 28, 17, 45, 29)
        print("datetime(2013, 10, 28, 17, 45, 29) = {}".format(d))

        x = datetime.datetime.today()
        print("datetime.today() = {}".format(x))

        x = datetime.datetime.now()
        print("datetime.now() = {}".format(x))

        x = datetime.datetime.utcnow()
        print("datetime.utcnow() = {}".format(x))

        x = datetime.datetime.fromtimestamp(1239456789)
        print("datetime.fromtimestamp(1239456789) = {}".format(x))

        x = datetime.datetime.utcfromtimestamp(347283)
        print("datetime.utcfromtimestamp(347283) = {}".format(x))
        
        t = datetime.time(17, 31, 10, 391)
        x = datetime.datetime.combine(d, t)
        print("datetime.combine('date', 'time') = {}".format(x))

        x = d.strptime("2013 11", "%Y %m")
        print("({}) datetime.strptime('2013 11', '%Y %m') = {}".format(d, x))
        
        print("\nTime object")

        t = datetime.time(21, 54, 11, 2318)
        print("datetime.time(21, 54, 11) = {}".format(t))

        y = t.min
        print("datetime.min = {}".format(y))

        y = t.max
        print("datetime.max = {}".format(y))

        y = t.resolution
        print("datetime.resolution = {}".format(y))

        y = t.hour
        print("datetime.hour = {}".format(y))

        y = t.minute
        print("datetime.minute = {}".format(y))

        y = t.second
        print("datetime.second = {}".format(y))

        y = t.microsecond
        print("datetime.microsecond = {}".format(y))

        y = t.tzinfo
        print("datetime.tzinfo = {}".format(y))

        y = t.replace(hour=7, second=21)
        print("({}) datetime.replace(hour=7, seconds=21) = {}".format(t, y))

        y = t.isoformat()
        print("datetime.isoformat = {}".format(y))

        y = t.utcoffset()
        print("datetime.utcoffset = {}".format(y))

        y = t.dst()
        print("datetime.dst = {}".format(y))

if __name__ == '__main__':
    DatetimeTest().main()
