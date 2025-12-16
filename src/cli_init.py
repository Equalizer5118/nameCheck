'''
command used for testing
"/mnt/86DCD62ADCD613F1/Github repos/nameCheck/.venv/bin/python" "/mnt/86DCD62ADCD613F1/Github repos/nameCheck/src/main.py" cli --debug  --pglist "/mnt/86DCD62ADCD613F1/Github repos/nameCheck/src/Synergy.xlsx" --ybalist "/mnt/86DCD62ADCD613F1/Github repos/nameCheck/src/YBA.xlsx" --pgsheet "QRY801" --ybasheet "students" --nolog --pglastcol "Last" --pgfirstcol "First"
'''
# TODO: Save settings to JSON file
import sys
import qt_adv_vars as a
from spreadsheetms import init_sheet
from debugprint import p
from pathlib import Path
from pandas.core.frame import DataFrame
from nameCheck import *

def panic(msg):
    # General error function. Simple enough, plug in msg, output error + help txt.
    print(f'Error: {msg}')
    print(a.helptxt)
    input('Press enter to exit...')
    quit()

def get_sett(arg, expected):
    # Attempts to get the setting
    try:
        val = sys.argv[sys.argv.index(arg) + 1]
    except IndexError:
        panic(f'No value provided for argument {arg}')
    if val[:2] == '-': panic(f'Invalid argument provided for {arg}: {val} Expected: {expected}') 
    # Could break if a folder name begins with a dash. || TODO: Change to where 
    # all supported args are in a list, and this compares the setting to that list. 
    # Also could then use similar logic to check if there are any unsupported args
    return val                                                                                   
def test_path(arg, expected):                                                                    

    val = get_sett(arg = arg, expected = expected)
    path = Path(val)
    if Path.is_file(path):
        return path
    panic(f'Invalid argument provided for {arg}: {val} Expected: {expected}')

def test_sheet(listpath, sheetname):
    listn = init_sheet(listpath, sheetname)
    p(type(listn))
    if type(listn) != DataFrame: panic(listn)

def cli_init():
    p('CLI mode detected')
    mode = 'standard'
    if '--json' in sys.argv:
        mode = 'json'
        p('JSON file used')
    
    parse_clargs(mode)
    if '--nocheck' in sys.argv or '-nc' in sys.argv: 
        input('Press enter to exit the program...')
        quit()
    checkNames1()
    checkNames2()
    checkNames3()

def parse_clargs(mode):
    if mode == 'json':
        from json_loading import import_json
        jfile = sys.argv[sys.argv.index('--json')]
        # Confirm json file is valid
        path = test_path(jfile, '[path].json')
        print('Importing settings from json file...')

        import_json(path)

        # Verify everything exists
        if not (Path(a.pgclist).is_file() or Path(a.ybaclist).is_file()): panic('One or more lists provided in JSON do not exist')
        test_sheet(a.pgclist, a.pgcsheet)
        test_sheet(a.ybaclist, a.ybacsheet)

    else:
        p('Sanity Checking required command line arguments...')
        if not ('--ybasheet' and '--ybalist' and '--pgsheet' and '--pglist') in sys.argv:
            panic('''Missing one or more required arguments. Please provide the following arguments:
            --pglist [path]: Path to the roster spreadsheet (.xls(x)/.ods)
            --pgsheet [name]: Name of the roster sheet to check
            --ybalist [path]: Path to the YBA spreadsheet (.xls(x)/.ods)
            --ybasheet [name]: Name of the YBA sheet to check''')

        # Required Command line arguments

        # Parse command line list arguments. This method works, it may not be the fastest but it works for now. || TODO: Improve this logic using functions, not iterating every time like a dumbass
        for i in range(len(sys.argv)):
            p(f'Iteration {i}: {sys.argv[i]}')
            if sys.argv[i] == ('--pglist') or sys.argv[i] == ('--ybalist'):
                p('Found list argument')
                # Validate path
                path = test_path(sys.argv[i], '[path].xls(x)/.ods')

                if sys.argv[i] == '--pglist':
                    a.pgclist = path
                    p('PG list set')
                elif sys.argv[i] == '--ybalist':
                    a.ybaclist = path
                    p('YBA list set')
        
        # Parse command line sheet arguments
        for i in range(len(sys.argv)):
            p(f'Iteration {i}: {sys.argv[i]}')
            if sys.argv[i] == ('--pgsheet') or sys.argv[i] == ('--ybasheet'):
                p('Found sheet argument')
                # Try getting sheet name
                try:  
                    sheetname = sys.argv[i + 1]
                except IndexError:
                    panic(f'No value provided for argument {sheetname}')
                
                # Validate sheet by trying to open it
                if sys.argv[i] == '--pgsheet':
                    test_sheet(a.pgclist, sheetname)
                    a.pgcsheet = sheetname
                    p('PG sheet set')
                elif sys.argv[i] == '--ybasheet':
                    test_sheet(a.ybaclist, sheetname)
                    a.ybacsheet = sheetname
                    p('YBA sheet set')

        # Optional Args
        if '--nolog' in sys.argv:
            a.genlog = 0
        
        # PG specific args
        if '--pgfirstcol' in sys.argv:
            # First name Column
            colfirst = sys.argv[sys.argv.index('--pgfirstcol')]
            a.pg_firstcol = get_sett(colfirst, 'string')
        if '--pglastcol' in sys.argv:
            collast = sys.argv[sys.argv.index('--pglastcol')]
            a.pg_lastcol = get_sett(collast, 'string')
        if '--pggradesepcol' in sys.argv and '--pggradesepvar' in sys.argv:
            a.pg_gradecos = 'Column'

            gradesepcol = sys.argv[sys.argv.index('--pggradesepcol')]
            a.pg_gradesep = get_sett(gradesepcol, 'string')

            gradesepvar = sys.argv[sys.argv.index('--pggradesepvar')]
            a.pg_gradesepv = get_sett(gradesepvar, 'string')
        
        elif '--pggradesepcol' in sys.argv or '--pggradesepvar' in sys.argv:
            # Catch if only one is present. Theres probably a better way to do this, but i cant be bothered rn
            panic('Both "--pggradesepcol" and "--pggradesepvar" need to be defined in order to use the colum grade seperator function.')

        # YBA specific args
        if '--ybafirstcol' in sys.argv:
            # First name Column
            colfirst = sys.argv[sys.argv.index('--ybafirstcol')]
            a.yba_firstcol = get_sett(colfirst, 'string')
        if '--ybalastcol' in sys.argv:
            collast = sys.argv[sys.argv.index('--ybalastcol')]
            a.yba_lastcol = get_sett(collast, 'string')
        if '--ybagradesepcol' in sys.argv and '--ybagradesepvar' in sys.argv:
            a.yba_gradecos = 'Column'

            gradesepcol = sys.argv[sys.argv.index('--ybagradesepcol')]
            a.yba_gradesep = get_sett(gradesepcol, 'string')

            gradesepvar = sys.argv[sys.argv.index('--ybagradesepvar')]
            a.yba_gradesepv = get_sett(gradesepvar, 'string')
        
        elif '--ybagradesepcol' in sys.argv or '--ybagradesepvar' in sys.argv:
            # Catch if only one is present. Theres probably a better way to do this, but i cant be bothered rn
            panic('Both "--ybagradesepcol" and "--ybagradesepvar" need to be defined in order to use the colum grade seperator function.')


        
                
                
            
    print(f'PG sheet: {a.pgcsheet}, PG list: {a.pgclist}')
    print(f'YBA sheet: {a.ybacsheet}, YBA list: {a.ybaclist}')



