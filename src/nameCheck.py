from pathlib import Path as path
from datetime import datetime as dt
from math import isnan
import spreadsheetms as si
import writelog as wl
from debugprint import p
import qt_adv_vars as a

def echo():
    print('nameCheck present')

def checkNames1():
    # Init variables
    a.unac = []
    a.noimg = []
    a.verified = []
    a.pgs = []
    a.ybas = []
    a.dat = dt.now()
    a.logfile = path('log.txt')
    a.log = ''

    a.pglist = si.init_pg(a.pgclist, a.pgcsheet)
    a.ybalist = si.init_yba(a.ybaclist, a.ybacsheet)

    a.pgi = a.pglist.index
    a.ybai = a.ybalist.index

    if a.logfile.exists() == False: a.logfile.open("x")

    # Add student names to lists
    for i in a.pgi: 
        if a.pg_gradecos == 'Column' and int(a.pglist.loc[i, a.pg_gradesep]) != int(a.pg_gradesepv):
            p(f'Name doesnt fir criteria, tossing. checked {a.pg_gradesep} and got {int(a.pglist.loc[i, a.pg_gradesep])}, should have gotten {int(a.pg_gradesepv)}.')
        else: 
            a.pgs.append(f'{a.pglist.loc[i, a.pg_lastcol]}, {a.pglist.loc[i, a.pg_firstcol]}')
    for i in a.ybai: 
        if a.yba_gradecos == 'Column' and int(a.ybalist.loc[i, a.yba_gradesep]) != int(a.yba_gradesepv):
            p(f'Name doesnt fir criteria, tossing. checked {a.yba_gradesep} and got {int(a.ybalist.loc[i, a.yba_gradesep])}, should have gotten {int(a.yba_gradesepv)}.')
        else: 
            a.ybas.append(f'{a.ybalist.loc[i, a.yba_lastcol]}, {a.ybalist.loc[i, a.yba_firstcol]}')

    # Last check to see if this is boken
    if len(a.pgs) == 0:
        raise ValueError('Length of pgs == 0. Check your Column var in Advanced options!')
    elif len(a.ybas) == 0:
        raise ValueError('Length of ybas == 0. Check your Column var in Advanced options!')

def checkNames2():
    # Name check
    for i in a.ybai:
        if a.ybas[i] in a.pgs:
            a.verified.append(a.ybas[i])
            p(a.ybalist.loc[i, 'Used on Page(s)'])
            try:
                int(a.ybalist.loc[i, 'Used on Page(s)'])
            except:
                p("ruh roh")
                try:
                    isnan(a.ybalist.loc[i, 'Used on Page(s)'])
                    a.noimg.append(a.ybas[i])
                except:
                    p("no ruh roh")
            a.pgs.remove(a.ybas[i])
        else:
            a.unac.append(f'{i}, {a.ybas[i]}')

def checkNames3():
    results = f'In total: {len(a.verified)}/{len(a.pgi)} students were verified leaving {len(a.unac)} unverified students in Yearbook Avenue, and {len(a.noimg)}/{len(a.verified)} verified students had untagged images.\n' \
      f'Additionally, {len(a.pgs)} students were either not in Yearbook Avenue or otherwise failed to verify, or could have multiple last names'
    # Initial Results
    p('')
    p(results)
    p('')

    # Write log
    if a.genlog: 
        wl.write_log(a.dat, a.verified, a.unac, a.pgs, a.noimg, a.pgi, a.logfile)
        log = 'Full list of students (un)verified/untagged/not-in-yba in log.txt file.'
    else:
        log = ''
    p('nameCheck complete')
    return f'{results}, \n {log}'
