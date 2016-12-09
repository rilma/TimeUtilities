if __name__ == '__main__':
    
    def example02():

        """ Coord. of the subsolar point """

        from datetime import datetime
        from timeutil.timeutil import TimeUtilities

        dtObj = TimeUtilities()
        print(dtObj.SubSol(datetime(2004,11,21,17,0,0)))
        

    example02()