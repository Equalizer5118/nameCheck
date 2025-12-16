import json
import pathlib
from debugprint import p
import qt_adv_vars as a
from pathlib import Path
import os

def import_json(name='default.json'):
    try:
        if pathlib.Path(os.path.abspath(name)).is_file():
            with open(name) as file:
                d = json.load(file)
                a.last_dir = d['last_dir']

                a.pgclist = d['pgclist']
                a.pgcsheet = d['pgcsheet']

                a.ybaclist = d['ybaclist']
                a.ybacsheet = d['ybacsheet']

                a.genlog = d['genlog']

                # PG sheet Adv values
                a.pg_lastcol = d['pg_lastcol']
                a.pg_firstcol = d['pg_firstcol']
                a.pg_gradecos = d['pg_gradecos']
                a.pg_gradesep = d['pg_gradesep']
                a.pg_gradesepv = d['pg_gradesepv']

                # PG sheet adv values
                a.yba_lastcol = d['yba_lastcol']
                a.yba_firstcol = d['yba_firstcol']
                a.yba_gradecos = d['yba_gradecos']
                a.yba_gradesep = d['yba_gradesep']
                a.yba_gradesepv = d['yba_gradesepv']
                a.dontshowdupe = d['dontshowdupe']
            p(f'Loaded saved settings from "{name}"')
            return f'Loaded saved settings from "{name}"'
        else:
            p(f'{name} is not a file!')
            return f'{name} is not a file!'
    except TypeError:
        p(f'{name} is not a valid filepath!')
        return f'{name} is not a valid filepath!'

def export_json(name):
    try:
        if pathlib.Path(os.path.abspath(name)).is_file() == False:
            if pathlib.Path(os.path.abspath(name)).is_dir():
                p(f'{name} is not a file!')
                return f'{name} is not a file!'
            else:
                open(Path(name), 'x')
                
        x = {
            'last_dir': a.last_dir,
            'pgclist': a.pgclist,
            'pgcsheet': a.pgcsheet,
            'ybaclist': a.ybaclist,
            'ybacsheet': a.ybacsheet,
            'genlog': a.genlog,
            'pg_lastcol': a.pg_lastcol,
            'pg_firstcol': a.pg_firstcol,
            'pg_gradecos': a.pg_gradecos,
            'pg_gradesep': a.pg_gradesep,
            "pg_gradesepv": a.pg_gradesepv,
            'yba_lastcol': a.yba_lastcol,
            'yba_firstcol': a.yba_firstcol,
            'yba_gradecos': a.yba_gradecos,
            'yba_gradesep': a.yba_gradesep,
            "yba_gradesepv": a.yba_gradesepv,
            'dontshowdupe': a.dontshowdupe,
        }
        with open(Path(os.path.abspath(name)), 'w') as f:
            json.dump(x, f, indent=4)
        p(f'Saved settings to "{name}"')
        return f'Saved settings to "{name}"'
    except TypeError:
        p(f'{name} is not a valid filepath!')
        return f'{name} is not a valid filepath!'