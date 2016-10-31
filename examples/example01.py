
from timeutil.timeutil import TimeUtilities

if __name__ == '__main__':

    """ Examples
    """

    Obj = TimeUtilities()

    # Return number of days since 0001-01-01 00:00:00 UTC 
    print(Obj.ToTime(2004,11,9))

    # Return day of year
    print(Obj.CalcDOY(2004,11,9))

    # Verify if year is leap
    print(Obj.IsLeapYear(2005))

    # Return month and day of month
    print(Obj.CalcMDOM(314, 2004))

    # Return the time in the Moon
    print(Obj.ToMoonTime(2004,11,9))

    # Convert hour in floating-point number in hour, minute, second (integers)
    print(Obj.ToHMS(10.735))

    # Convert UTC to local time
    print(Obj.UT2LT(12.,-75,2004,314))

    # Return x-axis label for a given time interval in number of days since 0001-01-01 00:00:00 UTC
    print(Obj.TimeLabel([Obj.ToTime(2004,11,9), Obj.ToTime(2004,11,9,23,59,59)]))

    # Return the number of days since 0001-01-01 00:00:00 UTC given the number of seconds since Unix time
    print(Obj.S2DN(1e6))

    # Return Gregorian date
    print(Obj.GD2JD(2014,11,9))

    # Return Julian date
    print(Obj.JD2GD(Obj.GD2JD(2014,11,9,0)))

