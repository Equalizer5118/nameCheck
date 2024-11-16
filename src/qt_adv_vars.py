import json
import pathlib
from debugprint import p
'''
TODO:
    Config loading
    Make nameCheck.py read these
    Put paths and sheet names in here
    Config saving
'''

last_dir = '.'

pg_or_yba = 'pg'

pgclist = ''
pgcsheet = ''

ybaclist = ''
ybacsheet = ''

genlog = True

# PG sheet Adv values
pg_lastcol = 'Last Name'
pg_firstcol = 'First Name'
pg_gradecos = 'Sheet'
pg_gradesep = ''
pg_gradesepv = ''

# PG sheet adv values
yba_lastcol = 'Last Name'
yba_firstcol = 'First Name'
yba_gradecos = 'Sheet'
yba_gradesep = ''
yba_gradesepv = ''

taggedcol = 'Used on Page(s)'

if pathlib.Path.is_file(pathlib.Path('default.json')):
    with open('default.json') as file:
        print('Loaded saved settings')
        d = json.load(file)
        last_dir = d['last_dir']

        pgclist = d['pgclist']
        pgcsheet = d['pgcsheet']

        ybaclist = d['ybaclist']
        ybacsheet = d['ybacsheet']

        genlog = d['genlog']

        # PG sheet Adv values
        pg_lastcol = d['pg_lastcol']
        pg_firstcol = d['pg_firstcol']
        pg_gradecos = d['pg_gradecos']
        pg_gradesep = d['pg_gradesep']
        pg_gradesepv = d['pg_gradesepv']
        
        # PG sheet adv values
        yba_lastcol = d['yba_lastcol']
        yba_firstcol = d['yba_firstcol']
        yba_gradecos = d['yba_gradecos']
        yba_gradesep = d['yba_gradesep']
        yba_gradesepv = d['yba_gradesepv']

def export_json(name):
    x = {
        'last_dir': last_dir,
        'pgclist': pgclist,
        'pgcsheet': pgcsheet,
        'ybaclist': ybaclist,
        'ybacsheet': ybacsheet,
        'genlog': genlog,
        'pg_lastcol': pg_lastcol,
        'pg_firstcol': pg_firstcol,
        'pg_gradecos': pg_gradecos,
        'pg_gradesep': pg_gradesep,
        "pg_gradesepv": pg_gradesepv,
        'yba_lastcol': yba_lastcol,
        'yba_firstcol': yba_firstcol,
        'yba_gradecos': yba_gradecos,
        'yba_gradesep': yba_gradesep,
        "yba_gradesepv": yba_gradesepv,
    }
    with open(f'{name}.json', 'w') as f:
        json.dump(x, f, indent=4)
    p('default.json saved!')