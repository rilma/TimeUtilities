
import datetime
import matplotlib.dates
import numpy
import pylab


def caldat(tinput):
 tinput = numpy.atleast_1d(tinput)
 year = []; month = []; dom = []; hour = []; minute = []; second = [];
 for i in range(len(tinput)):
  dtobj = matplotlib.dates.num2date(tinput[i])
  year = numpy.append(year, dtobj.year); month = numpy.append(month, dtobj.month);
  dom = numpy.append(dom, dtobj.day); hour = numpy.append(hour, dtobj.hour);
  minute = numpy.append(minute, dtobj.minute); second = numpy.append(second, dtobj.second);
 return(year, month, dom, hour, minute, second)


def calc_mdom(doy, year):
    
    """
        Give the "day of the year" (doy) and "year" (year) numbers, provides 
        values of "month" (curr_month) and "day of the month" (curr_dom)
        
        Syntaxis:        
            month, dom = calc_mdom( doy, year )
        
    """
    
    fmdoy = []
    
    for i in range( 12 ):
        fmdoy = numpy.append( fmdoy, \
            numpy.atleast_1d( calc_doy( year, i + 1, 1 ) )[ 0 ])
        
    ind = numpy.where( fmdoy <= doy )
    curr_month = numpy.max( ind[ 0 ] ) + 1
    curr_dom = doy - fmdoy[ numpy.max( ind[ 0 ] ) ] + 1
 
    return( int(curr_month ), int( curr_dom ) )
    
#
# End of 'calc_mdom'
#####
    

def is_leap_year(year):
    d0 = totime(year, 1, 1, 0, 0, 0); df = totime(year, 12, 31, 0, 0, 0);
    output = 1. if ((df - d0) == 365) else 0.
    return(output)
 
def calc_doy(year, month, dom):
    curr_dtime = totime(year, month, dom, 0, 0, 0)
    init_dtime = totime(year, 1, 1, 0, 0, 0)    
    return(curr_dtime - init_dtime + 1.)
    
def totime(year, month, dom, hh=0, mm=0, ss=0, micsec=0):    
 dtime = []
    
 year = numpy.atleast_1d(year)
 month = numpy.atleast_1d(month)
 dom = numpy.atleast_1d(dom)
 minsec = numpy.atleast_1d(micsec)
    
 if (len(numpy.atleast_1d(hh)) == 1):
  hh = numpy.tile(hh, len(year)); mm = numpy.tile(mm, len(year));
  ss = numpy.tile(ss, len(year)); micsec = numpy.tile(micsec, len(year));
 if (len(numpy.atleast_1d(ss)) == 1):
  ss = numpy.tile(ss, len(year)); micsec = numpy.tile(micsec, len(year));
 for k in range(len(year)):
  dobj = datetime.date(int(year[k]), int(month[k]), int(dom[k]))
  #print long(micsec[k])
  tobj = datetime.time(int(hh[k]), int(mm[k]), int(ss[k]), long(micsec[k]))
  dt = datetime.datetime.combine(dobj, tobj)
  dtime.append(dt)
 return(numpy.atleast_1d(numpy.squeeze(matplotlib.dates.date2num(dtime))))
    
#def totime2(year, day, hh=0, mm=0, ss=0):
###    #if (len(numpy.atleast_1(hh)) == 1):
###    #    year = numpy.tile(year, len(day)); day = numpy.tile(day, len(day));
###    #    hh = numpy.tile(hh, len(day)); mm = numpy.tile(mm, len(day));
###    #    ss = numpy.tile(ss, len(day));
#    #for k in range(len(day)):
#    dobj = datetime.date(year, 1, 1)
#    tobj = datetime.time(hh, mm, ss)
#    dt = datetime.datetime.combine(dobj, tobj)    
#    return(matplotlib.dates.date2num(dt) + day - 1.0)

def dtlim(yy=2004, mo=11, dd=9, hh=[0, 23], mi=[0, 59], ss=[0, 59]):

    year = [yy, yy] if isinstance(yy, int) else yy
    month = [mo, mo] if isinstance(mo, int) else mo
    dom = [dd, dd] if isinstance(dd, int) else dd
    hour = [hh, hh] if isinstance(hh, int) else hh
    minute = [mi, mi] if isinstance(mi, int) else mi
    second = [ss, ss] if isinstance(ss, int) else ss
    
    dobj0 = datetime.date(year[0], month[0], dom[0]) 
    dobjf = datetime.date(year[1], month[1], dom[1])
    
    tobj0 = datetime.time(hour[0], minute[0], second[0], 0)
    tobjf = datetime.time(hour[1], minute[1], second[1], 0)
    
    dt0 = datetime.datetime.combine(dobj0, tobj0)
    dtf = datetime.datetime.combine(dobjf, tobjf)
    
    dt = []; dt.append(dt0); dt.append(dtf);
    
    dt_num = matplotlib.dates.date2num(dt)
    
    output = dt_num[0] if (dt_num[0] == dt_num[1]) else dt_num
    
    return(output)

def dtbin(dtrange=dtlim(2008, 6, [14, 15], 0, 0, 0), step=60):
    # dtrange ...
    # step in seconds
    
    ndays = numpy.ceil(dtrange[1] - dtrange[0])
    dtbins = dtrange[0] + numpy.arange(0, ndays, step / (24.0*3600.0))
    
    ind = numpy.where((dtbins >= dtrange[0]) & (dtbins <= dtrange[1]))
    
    return(dtbins[ind])

def fillgaps1D(xvalues, yvalues, step):
    #
    # step in seconds
    #
    
    dtobj = matplotlib.dates.num2date([xvalues[0], xvalues[len(xvalues) - 1]])
    dtobj0 = datetime.datetime(dtobj[0].year, dtobj[0].month, dtobj[0].day, 0, 0, 0)
    dtobjf = datetime.datetime(dtobj[1].year, dtobj[1].month, dtobj[1].day, 23, 59, 59)
    dt_bin = dtbin(matplotlib.dates.date2num([dtobj0, dtobjf]), step)
    xvals = dt_bin; yvals = numpy.zeros(xvals.shape) + numpy.nan;
    for i in range(len(xvalues)):
        ind = numpy.where(dt_bin == xvalues[i])
        yvals[ind] = yvalues[i]
        
    return({'xvalues':xvals, 'yvalues':yvals})    

def time_label(dtrange, strutc='UT'):
    
    dtobj = matplotlib.dates.num2date(dtrange)
    
    if (numpy.floor(dtrange[1]) - numpy.floor(dtrange[0]) >= 1.0):
        tlabel = "%s-%s (%s)" % (dtobj[0].strftime('%m/%d'),\
                                dtobj[1].strftime('%d/%Y'), strutc)
        tfname = '%s-%s' % (dtobj[0].strftime('%Y%m%d'),\
                            dtobj[1].strftime('%Y%m%d'))
    else :
        tlabel = "%s (%s)" % (dtobj[0].strftime('%m/%d/%Y'), strutc)
        tfname = '%s' % dtobj[0].strftime('%Y%m%d')

    return({'tlabel':tlabel, 'tfname':tfname})
    
# Convert # of seconds from 1/1/1970 to number of days from 1/1/1
def s2dn(input):
    dtobj = datetime.date(1970, 1, 1)
    return(input / (24 * 3600.0) + matplotlib.dates.date2num(dtobj))

# Convert # Gregorian to Julian date
def gd2jd(year, month, dom, hour=12, minute=0, second=0):    
    ut = hour + minute / 60.0 + second / 3600.0
    total_seconds = hour * 3600.0 + minute * 60.0 + second
    fracday = total_seconds / 86400.0
    if ((100 * year + month -190002.5) > 0):
        sig = 1
    else:
        sig = -1
    jd = 367.0 * year - numpy.int(7 * (year + numpy.int((month + 9) / 12)) / 4) + \
        numpy.int(275 * month / 9) + dom + 1721013.5 + ut / 24 - 0.5 * sig + 0.5
    return(jd)
    
# Convert Julian to Greogorian time
def jd2gd(input):
    inseconds = 86400.0 * (input - gd2jd(1970, 1, 1, 0, 0, 0))
    return(s2dn(inseconds))

#
# Rotation 1 Day 1 in this sequence was assigned arbitrarily by J. Bartels to February 8, 1832.
# For reference, Bartels rotation 2270 started on November 2, 1999, at 00:00:00 UT.
# http://www.srl.caltech.edu/ACE/ASC/level2/timing_data.html#bartels
#
def bartels_calendar(dimension, drange, start):
        
    # creating the array of dates in bartels calendar
    ndays_brotation = 27 # no. of days in a bartels rotation
    bartels_dates = start + numpy.arange(dimension) * ndays_brotation
    
    for i in range(len(drange)):
        ind = numpy.where(bartels_dates <= drange[i])[0]
        bdt = bartels_dates[ind[len(ind) - 1]] if (len(ind) > 0) else numpy.nan
        rtn = (ind[len(ind) - 1] + 1) if (len(ind) > 0) else numpy.nan
        ostart = bdt if (i == 0) else numpy.append(ostart, bdt)
        orotation = rtn if (i == 0) else numpy.append(orotation, rtn)
    
    return({'start':ostart, 'rotation':orotation})
    
def ut2lt(ut, glon, iyyy, ddd):
    xlon = glon
    if (glon > 180.):
        xlon = glon - 360.
    slt = ut + xlon / 15.
    if ((slt >= 0.) & (slt <= 24.)):
        return(slt)
    if (slt > 24.):
        slt = slt - 24.
        ddd = ddd + 1.
        dddend = 365.
        if (iyyy /4. * 4. == iyyy):
            dddend = 366.
        if (ddd > dddend):
            iyyy = iyyy + 1.
            ddd = 1.
        return(stl)
    slt = slt + 24.
    ddd = ddd - 1.
    if (ddd < 1.):
        iyyy = iyyy - 1.
        ddd = 365.
        # leap year if evenly divisible by 4 and not by 100, except if evenly
        # divisible by 400. Thus 2000 will be a leap year.
        if (iyyy / 4. * 4. == iyyy):
            ddd = 366.
    return(slt)
        
#        subroutine ut_lt(mode,ut,slt,glong,iyyy,ddd)
#c -----------------------------------------------------------------
#c Converts Universal Time UT (decimal hours) into Solar Local Time
#c SLT (decimal hours) for given date (iyyy is year, e.g. 1995; ddd
#c is day of year, e.g. 1 for Jan 1) and geodatic longitude in degrees.
#C For mode=0 UT->LT and for mode=1 LT->UT
#c Please NOTE that iyyy and ddd are input as well as output parameters
#c since the determined LT may be for a day before or after the UT day.
#c ------------------------------------------------- bilitza nov 95
#        integer         ddd,dddend
#
#        xlong=glong
#        if(glong.gt.180) xlong=glong-360
#        if(mode.ne.0) goto 1
#c
#c UT ---> LT
#c
#        SLT=UT+xlong/15.
#        if((SLT.ge.0.).and.(SLT.le.24.)) goto 2
#        if(SLT.gt.24.) goto 3
#                SLT=SLT+24.
#                ddd=ddd-1
#                if(ddd.lt.1.) then
#                        iyyy=iyyy-1
#                        ddd=365
#c
#c leap year if evenly divisible by 4 and not by 100, except if evenly
#c divisible by 400. Thus 2000 will be a leap year.
#c
#                        if(iyyy/4*4.eq.iyyy) ddd=366
#                        endif
#                goto 2
#3               SLT=SLT-24.
#                ddd=ddd+1
#                dddend=365
#                if(iyyy/4*4.eq.iyyy) dddend=366
#                if(ddd.gt.dddend) then
#                        iyyy=iyyy+1
#                        ddd=1
#                        endif
#                goto 2
#c
#c LT ---> UT
#c
#1       UT=SLT-xlong/15.
#        if((UT.ge.0.).and.(UT.le.24.)) goto 2
#        if(UT.gt.24.) goto 5
#                UT=UT+24.
#                ddd=ddd-1
#                if(ddd.lt.1.) then
#                        iyyy=iyyy-1
#                        ddd=365
#                        if(iyyy/4*4.eq.iyyy) ddd=366
#                        endif
#                goto 2
#5               UT=UT-24.
#                ddd=ddd+1
#                dddend=365
#                if(iyyy/4*4.eq.iyyy) dddend=366
#                if(ddd.gt.dddend) then
#                        iyyy=iyyy+1
#                        ddd=1
#                        endif
#2       return
#        end


def tohms(hr):

# Converts hr float-value into [hour, minute, second]

 hh_f = hr
 hh = int(pylab.floor(hh_f))

 mm_f = 60. * (hr - float(hh))
 mm = int(pylab.floor(mm_f))

 ss_f = 60. * (mm_f - float(mm))
 ss = int(pylab.floor(ss_f))
 
 return hh, mm, ss
#
# End of 'tohms'
#####


def toMoonTime( year=2003, month=11, dom=21, hour=12, minute=0, second=0 ):

    """ 
        Convert Earth's time to lunar clock
        
        Details on conversion at:        
        http://lunarclock.org/lunar-clock.php
        
        Results can be verified with "Convert a date to Lunar standard" 
        available at:
        http://lunarclock.org/convert-to-lunar-standard-time.php
        
    """    
        
    #import time_utilities as time_util

    # Time to be converted ...
    #ts = time_util.totime( year, month, dom, hour, minute, second, 0 )[ 0 ]    
    ts = totime( year, month, dom, hour, minute, second, 0 )[ 0 ]    

    # Neil Armstron set foot on the Moon on July 21st, 1969 at 02:56:15 UT so 
    # this is the point in time for the calendar to start
    #t0 = time_util.totime( 1969, 7, 21, 2, 56, 15, 0 )[ 0 ]
    t0 = totime( 1969, 7, 21, 2, 56, 15, 0 )[ 0 ]

    tlp = ( ts - t0 ) / ( 24. * 3600. )
    
    # a lunar second in terrestrial seconds
    lsec2tsec = 0.9843529666671

    # lunar cycle to terrestrial seconds
    lcy2tsec = 24 * 60 * 60 * lsec2tsec
    
    # Time lapsed in number of lunar cycles
    tlp = ( ts - t0 ) *  24 * 60 * 60 / lcy2tsec
    
    # As 't0' represents 01-01-01 'nabla' 00:00:00, I add 1 lunar year, 
    # 1 lunar day, and 1 lunar cycle, in lunar cycle units
    tlp += 12 * 30 + 30 + 1

    # from lunar cycles to lunar hour
    dummy = ( tlp - pylab.floor( tlp ) ) * 24
    lhour = int( pylab.floor( dummy ) )
    
    # from lunar hour to lunar minute
    dummy = ( dummy - pylab.floor( dummy ) ) * 60
    lminute = int( pylab.floor( dummy ) ) 
    
    # from lunar minutes to lunar seconds
    dummy = ( dummy - pylab.floor( dummy ) ) * 60
    lsecond = int( pylab.floor( dummy ) )     

    # lunar year
    dummy = tlp / ( 12. * 30.)
    lyear = int( pylab.floor( dummy ) )
    
    # lunar day
    dummy = (dummy - pylab.floor( dummy ) ) * 12
    lday = int( pylab.floor( dummy ) )
    
    # lunar cycle
    dummy = (dummy - pylab.floor( dummy ) ) * 30
    lcycle = int( pylab.floor( dummy ) )    

    #print lyear, lday, lcycle
    #print lhour, lminute, lsecond    
        
    return ( lyear, lday, lcycle, lhour, lminute, lsecond )
#
# End of 'toMoonTime'
#####
    