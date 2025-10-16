from pathlib import Path as path
from datetime import datetime as dt
from math import isnan
import spreadsheetms as si
import writelog as wl
from debugprint import p
import qt_adv_vars as a

def echo():
    print('nameCheck present')



def catchLastNameSimilarity():
    p()
        # BC my school's admin is fucking stupid, they give us gov names and not preferred names. As stupid as this is, we have to catch it otherwise yearbooks will get recalled
        # This checks names in the not in YBA list and compares to the unverified list (doesnt check verified list, as not needed),
        # 1700 yearbooks recalled for 1 name, who wasn't even in the yearbook other than that person's portrait image... 

    for i in a.pgs:
        listsave = []
        unverif_names = []
        sim = 0

        checkto_raw = i
        p(checkto_raw)
        checkto_cpos = checkto_raw.find(',')
        checkto = checkto_raw[0:checkto_cpos]
        p(checkto)

        for o in a.unac:
            checkagn_raw = o
            p(checkagn_raw)
            checkagn_cpos = checkagn_raw.find(',')
            checkagn = checkagn_raw[0:checkagn_cpos]
            p(checkagn)
            if checkto == checkagn:
                sim = 1
                p('Simlilar name, appending to list')
                unverif_names.append(checkagn_raw)
        
        if sim == 1:
            listsave = f'Name on Roster: "{checkto_raw}"     Similar names: "{unverif_names}"'
            p(listsave)
            a.namesim.append(listsave)
        else:
            p('No names are similar, passing')
            

def checkNames1():
    # Init variables
    a.unac = [] # unverified students
    a.noimg = [] # students verified with no images
    a.verified = [] # verified with at least portrait
    a.pgs = [] # students in roster to check, after nameCheck2() this turns into the students who are not in YBA
    a.ybas = [] # students in YBA to check
    a.dat = dt.now() # date
    a.logfile = path('log.txt') # log file path and name
    a.log = '' # init log file text (is this needed?)

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
    a.pgmid = len(a.pgs)
    # Last check to see if this is boken
    if len(a.pgs) == 0:
        raise ValueError('Length of pgs == 0. Check your Column var in Advanced options!')
    elif len(a.ybas) == 0:
        raise ValueError('Length of ybas == 0. Check your Column var in Advanced options!')

def checkNames2():
    # Name check
    i = 1
    while i < len(a.ybas):
        p(i)
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
            a.unac.append(f'{a.ybas[i]}')
        i += 1

def checkNames3():
    if len(a.pgs) != 0:
        catchLastNameSimilarity() # Rosalie to Ross, I hate you admin office...
    else: 
        p('No Unverified names, skipping similarity check')
    
    results = f'In total: {len(a.verified)}/{a.pgmid} students were verified leaving {len(a.unac)} unverified students in Yearbook Avenue, and {len(a.noimg)}/{len(a.verified)} verified students had untagged images.\n' \
      f'Additionally, {len(a.pgs)} students were either not in Yearbook Avenue or otherwise failed to verify, or could have multiple last names, with {len(a.namesim)} of those names having possible matches'
    # Initial Results
    p('')
    p(results)
    p('')

    # Write log
    if a.genlog: 
        wl.write_log(a.dat, a.verified, a.unac, a.pgs, a.noimg, results, a.logfile, a.pgclist, a.pgcsheet, a.ybaclist, a.ybacsheet, a.namesim)
        log = 'Full list of students (un)verified/untagged/not-in-yba in log.txt file.'
    else:
        log = ''
    p('nameCheck complete')
    return f'{results}, \n{log}'
