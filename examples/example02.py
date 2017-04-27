#!/usr/bin/env python

def example02():

    """ Coord. of the subsolar point """

    from datetime import datetime
    from timeutil.timeutil import TimeUtilities

    dtObj = TimeUtilities()
    print(dtObj.SubSol(datetime(2004,11,21,17,0,0)))

if __name__ == '__main__':

    example02()