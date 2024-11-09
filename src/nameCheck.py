import pandas as pd
#from readchar import readchar
from pathlib import Path as path
from datetime import datetime as dt
from math import isnan
import configparser

# COMMAND TEST
#print(float('nan'))
#print(float('nan') == float('none'))
#quit()
# ======

#config stuffs
config = configparser.ConfigParser()
def create_config():
    config['PATHS'] = {'pg_class_roster': 'path_to_PGlist_here', 'yba_class_covrep': 'path_to_yba_class_covrep'}
    config['SHEETNAMES'] = {'roster_sheet_name': '0', 'covrep_sheet_name': '0'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print('No config file found, created empty template. Please add paths to the spreadsheets in "config.ini" before proceeding!')
    k = input("")
    quit()
# Create config.ini if missing
if not path.exists(path('config.ini')): 
    create_config()
else: config.read('config.ini')

# Init variables
unac = []
noimg = []
verified = []
pgs = []
ybas = []
dat = dt.now()
logfile = path('log.txt')
try:
    pglist = pd.read_excel(config['PATHS']['pg_class_roster'], sheet_name=config['SHEETNAMES']['roster_sheet_name'])
except:
    print('!!!!Path to/sheet name for pg roster invalid or missing in config file!')
    input("Press enter to exit the program...")
    exit()
try:
    ybalist = pd.read_excel(config['PATHS']['yba_class_covrep'], sheet_name=config['SHEETNAMES']['covrep_sheet_name'])
except:
    print('!!!!Path to/sheet name for YBA coverage report invalid or missing in config file!')
    input("Press enter to exit the program")
    exit()
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
        print(ybalist.loc[i, 'Used on Page(s)'])
        try:
            int(ybalist.loc[i, 'Used on Page(s)'])
        except:
            print("ruh roh")
            try:
                isnan(ybalist.loc[i, 'Used on Page(s)'])
                noimg.append(ybas[i])
            except:
                print("no ruh roh")
 #       if isnan(ybalist.loc[i, 'Used on Page(s)']) and ',' not in ybalist.loc[i, 'Used on Page(s)']:
 #           print('not a number, womp womp')
 #           noimg.append(ybas[i])
        pgs.remove(ybas[i])
    else:
        unac.append(f'{i}, {ybas[i]}')

# Initial Results
print('')
print(f'In total: {len(verified)}/{len(pgi)} students were verified leaving {len(unac)} unverified students in Yearbook Avenue, and {len(noimg)}/{len(verified)} verified students had untagged images.')
print(f'Additionally, {len(pgs)} students were either not in Yearbook Avenue or otherwise failed to verify, or could have multiple last names')
print('')

# Write log
bruthuh = '============================================================== \n' \
f'[{dat}] nameCheck Log:\n' \
'\n' \
f'Verified students: {verified}\n' \
'\n' \
'\n' \
'\n' \
f'YBA unverified students: {unac}\n' \
'\n' \
'\n' \
'\n' \
f'Not in YBA/misspelled: {pgs}\n' \
'\n' \
'\n' \
'\n' \
f'No tagged IMG: {noimg}\n' \
'\n' \
'\n' \
'\n' \
f'In total: {len(verified)}/{len(pgi)} students were verified leaving {len(unac)} unverified students in Yearbook Avenue, and {len(noimg)}/{len(verified)} verified students had untagged images. \n' \
f'Additionally, {len(pgs)} students were either not in Yearbook Avenue or otherwise failed to verify, or could have multiple last names. \n' \
'==============================================================\n' \
'\n'


with logfile.open("a") as file:
    file.write(bruthuh)

print('Full list of students (un)verified/untagged/not-in-yba in log.txt file.')
print('Press any key to exit...')
k = input()
#o = 0
#for l in ybalist.index:
#    loop = True
#    while loop:
#        if str(pglist.loc[l, 'Last Name']) != str(ybalist.loc[l+o, 'Last Name']) or pglist.loc[l, 'First Name'] != ybalist.loc[l+o, 'First Name']:
#            print(f'Name mismatch! Adding {ybalist.loc[l+o, 'Last Name']}, {ybalist.loc[l+o, 'First Name']} to list of unnacounted for names and incrementing offest by 1. now {o}')
#            unac.append(f'{ybalist.loc[l+o, 'Last Name']}, {ybalist.loc[l+o, 'First Name']}')
#            o += 1
#        else:
#            loop = False
#    print(f'{ybalist.loc[l+o, 'Last Name']}, {ybalist.loc[l+o, 'First Name']} is registered and accounted for')
#    ac.append(f'{ybalist.loc[l+o, 'Last Name']}, {ybalist.loc[l+o, 'First Name']}')
#    if l >= 20: exit()
