import pandas as pd
#from readchar import readchar
from pathlib import Path as path
from datetime import datetime as dt
from math import isnan
from qt_univerr import funcerror
import configcreate as cc
import configparser
import spreadsheetms as si
import writelog as wl
from debugprint import p
import qt_adv_vars as a

def echo():
    print('nameCheck present')

# COMMAND TEST
#p(float('nan'))
#p(float('nan') == float('none'))
#quit()
# ======
def checkNames():
    #config stuffs. Could use later.
    #config = configparser.ConfigParser()
    #cc.init_config()
    #config.read('config.ini')
    #pgclist = config['PATHS']['pg_class_roster']
    #pgcsheet = config['SHEETNAMES']['roster_sheet_name']
    #ybaclist = config['PATHS']['yba_class_covrep']
    #ybacsheet = config['SHEETNAMES']['covrep_sheet_name']
    # Init variables
    unac = []
    noimg = []
    verified = []
    pgs = []
    ybas = []
    dat = dt.now()
    logfile = path('log.txt')
    log = ''

    pglist = si.init_pg(a.pgclist, a.pgcsheet)
    ybalist = si.init_yba(a.ybaclist, a.ybacsheet)

    pgi = pglist.index
    ybai = ybalist.index

    if logfile.exists() == False: logfile.open("x")

    # Add student names to lists
    for i in pgi: 
        if a.pg_gradecos == 'Column' and int(pglist.loc[i, a.pg_gradesep]) != int(a.pg_gradesepv):
            p(f'Name doesnt fir criteria, tossing. checked {a.pg_gradesep} and got {int(pglist.loc[i, a.pg_gradesep])}, should have gotten {int(a.pg_gradesepv)}.')
        else: 
            pgs.append(f'{pglist.loc[i, a.pg_lastcol]}, {pglist.loc[i, a.pg_firstcol]}')
    for i in ybai: 
        if a.yba_gradecos == 'Column' and int(ybalist.loc[i, a.yba_gradesep]) != int(a.yba_gradesepv):
            p(f'Name doesnt fir criteria, tossing. checked {a.yba_gradesep} and got {int(ybalist.loc[i, a.yba_gradesep])}, should have gotten {int(a.yba_gradesepv)}.')
        else: 
            ybas.append(f'{ybalist.loc[i, a.yba_lastcol]}, {ybalist.loc[i, a.yba_firstcol]}')

    # Last check to see if this is boken
    if len(pgs) == 0:
        raise ValueError('Length of pgs == 0. Check your Column var in Advanced options!')
    elif len(ybas) == 0:
        raise ValueError('Length of ybas == 0. Check your Column var in Advanced options!')

    # Name check
    for i in ybai:
        if ybas[i] in pgs:
            verified.append(ybas[i])
            p(ybalist.loc[i, 'Used on Page(s)'])
            try:
                int(ybalist.loc[i, 'Used on Page(s)'])
            except:
                p("ruh roh")
                try:
                    isnan(ybalist.loc[i, 'Used on Page(s)'])
                    noimg.append(ybas[i])
                except:
                    p("no ruh roh")
            pgs.remove(ybas[i])
        else:
            unac.append(f'{i}, {ybas[i]}')

    results = f'In total: {len(verified)}/{len(pgi)} students were verified leaving {len(unac)} unverified students in Yearbook Avenue, and {len(noimg)}/{len(verified)} verified students had untagged images.\n' \
      f'Additionally, {len(pgs)} students were either not in Yearbook Avenue or otherwise failed to verify, or could have multiple last names'
    # Initial Results
    p('')
    p(results)
    p('')

    # Write log
    if a.genlog: 
        wl.write_log(dat, verified, unac, pgs, noimg, pgi, logfile)
        log = 'Full list of students (un)verified/untagged/not-in-yba in log.txt file.'

    p('nameCheck complete')
    return f'{results}, \n {log}'
    #p('Press any key to exit...')
    #k = input()
