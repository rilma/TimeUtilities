#!/usr/bin/env python

from datetime import datetime
from timeutil import TimeUtilities

def example02():

    """ Coord. of the subsolar point """

    dtObj = TimeUtilities()
    print(dtObj.SubSol(datetime(2004,11,21,17,0,0)))

if __name__ == '__main__':

    example02()