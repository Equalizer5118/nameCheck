import json
import pathlib
from debugprint import p
import qt_adv_vars as a
from pathlib import Path
import traceback
import os
from ver import ver

def json_load_GUI(name):
    from PySide6.QtWidgets import QMessageBox
    from qt_univerr import notice, funcerror
    res = import_json(name)
    if res[0] != 0:
        if res[0] == 3:
            reason = f'''JSON loading failed with the following error message
    Exit Code 3: Version Mismatch! JSON version: {res[1][1]}, Program version: {res[1][2]}.
The JSON file version does not match the current program version. If you proceed, some settings may not load correctly.
Do you want to proceed?'''
            msgbox = notice(icon = QMessageBox.Critical, title = 'JSON Import Error', reason = reason)
            msgbox.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
            msgbox.setDefaultButton(QMessageBox.StandardButton.Yes)
            ret = msgbox.exec()
            if ret == QMessageBox.StandardButton.Yes:
                print('Proceeding with JSON import attempt')
                from json_loading import json_to_vars
                json_to_vars(a.openjson)
            else:
                return [3, 'User aborted JSON import due to version mismatch']
        else:
            e = [res[0], res[1]]
            print(f'JSON import error: {e}')
            return e
    return [0, f'JSON load from {name} success']

def findsetting(key, d):
    try:
        p(f'Finding {key} in JSON. Set as {d[key]}')
        return d[key]
    except KeyError:
        p(f'Key "{key}" not found in JSON data!')
        return None

def json_to_vars(d):
    a.last_dir = findsetting('last_dir', d)

    a.pgclist = findsetting('pgclist', d)
    a.pgcsheet = findsetting('pgcsheet', d)
    p(a.pgcsheet)

    a.ybaclist = findsetting('ybaclist', d)
    a.ybacsheet = findsetting('ybacsheet', d)
    p(a.ybacsheet)

    a.dontshowdupe = findsetting('dontshowdupe', d)

    a.genlog = findsetting('genlog', d)

    # PG sheet Adv values
    a.pg_lastcol = findsetting('pg_lastcol', d)
    a.pg_firstcol = findsetting('pg_firstcol', d)
    a.pg_gradecos = findsetting('pg_gradecos', d)
    a.pg_gradesep = findsetting('pg_gradesep', d)
    a.pg_gradesepv = findsetting('pg_gradesepv', d)

    # PG sheet adv values
    a.yba_lastcol = findsetting('yba_lastcol', d)
    a.yba_firstcol = findsetting('yba_firstcol', d)
    a.yba_gradecos = findsetting('yba_gradecos', d)
    a.yba_gradesep = findsetting('yba_gradesep', d)
    a.yba_gradesepv = findsetting('yba_gradesepv', d)

    return [0, None]

def import_json(name=None, Pass = False): # name is set to none for easier cli use. Should have no effect on GUI
    if name is None: name = 'data/default.json' 
    try:
        if pathlib.Path(os.path.abspath(name)).is_file():
            with open(name) as file:
                a.openjson = json.load(file)
                try: version = a.openjson['version']
                except KeyError: version = 'unknown'
                if version != ver: return [3, ['Version Mismatch!', version, ver]]
                res = json_to_vars(a.openjson)
                p(f'Loaded settings from "{name}"')
                return res
                    
        else:
            p(f'{name} is not a file!')
            return [1, f'{name} is not a file!']
    except TypeError:
        p(f'{name} is not a valid filepath!')
        return [2, f'{name} is not a valid filepath!']

def export_json(name = None): # name is set to none for easier cli use. Should have no effect on GUI
    if name is None: name = 'data/default.json' 
    try:
        p(name)
        if pathlib.Path(os.path.abspath(name)).is_file() == False:
            if pathlib.Path(os.path.abspath(name)).is_dir():
                print(f'{name} points to a directory. Must point to an existing .json file or the name of a new .json file.')
                return 'Failed'
            else:
                open(Path(name), 'x')
                
        x = {
            'version': ver,
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
    except TypeError as te:
        print(f'{name} is not a valid filepath, or one or more objects could not be serialized!')
        if a.debug == 1:
            print(traceback.format_exc())
        else:
            print(f'TypeError: {te}')
        return 'Failed'