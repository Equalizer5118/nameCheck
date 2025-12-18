import pandas as pd
from debugprint import p
def echo():
    print('nameCheck present')
def init_sheet(list, pgcsheet, engine = 'openpyxl'):
    list = str(list) # Lists coming from CLI mode may be a PosixPath object and not a string. Force list to be a string.
    p(list)
    p(list[-3:])
    if list[-3:] == 'ods': engine = 'odf'
    try:
        rlist = pd.read_excel(list, sheet_name=pgcsheet, engine=engine)
    except FileNotFoundError:
        p(f'File not found: {list}')
        return f'File not found: {list}'
    except ValueError:
        p(f'Sheet name "{pgcsheet}" not found in file: {list}')
        return f'Sheet name "{pgcsheet}" not found in file: {list}'   
    return rlist
def test_sheet(listpath, sheetname):
    listn = init_sheet(listpath, sheetname)
    p(type(listn))
    if type(listn) != pd.DataFrame: 
        raise ValueError(
f'{sheetname} does not exist in {listpath}!'
        )