import pandas as pd
#from readchar import readchar
from pathlib import Path as path
from datetime import datetime as dt
from math import isnan
import configcreate as cc
import configparser
import spreadsheetms as si
import writelog as wl
from debugprint import p

def echo():
    print('nameCheck present')

# COMMAND TEST
#p(float('nan'))
#p(float('nan') == float('none'))
#quit()
# ======
def checkNames(pgclist, pgcsheet, ybaclist, ybacsheet, genlog):
    #config stuffs
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

    pglist = si.init_pg(pgclist, pgcsheet)
    ybalist = si.init_yba(ybaclist, ybacsheet)

    pgi = pglist.index
    ybai = ybalist.index

    if logfile.exists() == False: logfile.open("x")

    # Add student names to lists
    for i in pgi: pgs.append(f'{pglist.loc[i, 'Last Name']}, {pglist.loc[i, 'First Name']}')
    for i in ybai: ybas.append(f'{ybalist.loc[i, 'Last Name']}, {ybalist.loc[i, 'First Name']}')

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
    if genlog: 
        wl.write_log(dat, verified, unac, pgs, noimg, pgi, logfile)
        log = 'Full list of students (un)verified/untagged/not-in-yba in log.txt file.'

    p('nameCheck complete')
    return f'{results}, \n {log}'
    #p('Press any key to exit...')
    #k = input()
