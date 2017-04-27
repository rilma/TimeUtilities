from datetime import datetime
from numpy.testing import assert_allclose,run_module_suite,assert_equal
#
from timeutil import TimeUtilities


def test_time():
    Obj = TimeUtilities()

    # Return number of days since 0001-01-01 00:00:00 UTC
    assert_allclose(Obj.ToTime(2004,11,9), 731894.)

    # Return day of year
    assert Obj.CalcDOY(2004,11,9)==314

    # Verify if year is leap
    assert not Obj.IsLeapYear(2005)

    # Return month and day of month
    assert Obj.CalcMDOM(314, 2004)  == (11, 9)

    # Return the time in the Moon
    assert_equal(Obj.ToMoonTime(2004,11,9),(37, 5, 20, 20, 26, 2))

    # Convert hour in floating-point number in hour, minute, second (integers)
    assert Obj.ToHMS(10.735) == (10, 44, 5)

    # Convert UTC to local time
    assert_allclose(Obj.UT2LT(12.,-75,2004,314), 7.)

    # Return x-axis label for a given time interval in number of days since 0001-01-01 00:00:00 UTC
    assert_equal(Obj.TimeLabel([Obj.ToTime(2004,11,9),
                                Obj.ToTime(2004,11,9,23,59,59)]),
                                ('11/09/2004 (UT)', '20041109'))

    # Return the number of days since 0001-01-01 00:00:00 UTC given the number of seconds since Unix time
    assert_allclose(Obj.S2DN(1e6),719174.574074074)

    # Return Gregorian date
    assert_allclose(Obj.GD2JD(2014,11,9), 2456971.)

    # Return Julian date
    assert_allclose(Obj.JD2GD(Obj.GD2JD(2014,11,9,0)), 735546.)

    # Coord. of the subsolar point
    assert_allclose(Obj.SubSol(datetime(2004,11,21,17,0,0)),(-20.090326448802241, -78.493257756068147))

if __name__ == '__main__':
    run_module_suite()
