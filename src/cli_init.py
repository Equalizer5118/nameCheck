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
from spreadsheetms import test_sheet
import traceback


def cli_init():
    p('CLI mode detected')
    a.method = 'cli'
    mode = 'standard'
    if '--json' in sys.argv:
        mode = 'json'
        p('JSON file used')
    
    parse_clargs(mode)

    if '--savejson' in sys.argv:
        from json_loading import export_json
        epxjson = get_sett('--savejson', '[name].json', True) # Using get_sett and not test_path bc test/creation logic is handled in export_json
        result = export_json(epxjson)
        if result == 'Failed':
            panic('Failed to export settings to JSON. Check console history for more details.')
        print()

    if ('--nocheck' in sys.argv) or ('-nc' in sys.argv): return

    checkNames1()
    checkNames2()
    checkNames3()

def parse_clargs(mode):
    if mode == 'json':
        from json_loading import import_json
        jfile = sys.argv[sys.argv.index('--json')]
        # Confirm json file is valid
        path = get_sett(jfile, '[path].json', True)
        print('Importing settings from json file...')

        res = import_json(path)
        if res[0] != 0:
            print('Import failed with the following exit code:')
            if res[0] == 3:
                print(f'Exit Code 3: Version Mismatch! JSON version: {res[1][1]}, Program version: {res[1][2]}')
                print('The JSON file version does not match the current program version. If you proceed, some settings may not load correctly.')
                inp = input('Do you want to proceed? (y/n): ')
                if inp.lower() == 'y':
                    print('Proceeding with JSON import attempt')
                    from json_loading import json_to_vars
                    json_to_vars(a.openjson)
                else:
                    panic('Version mismatch.')
            else:
                print(f'Exit Code {res[0]}: {res[1]}')
                panic('Error during JSON import. See console output for more details.')
        print('JSON import successful, verifying settings') 

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

def panic(msg):
    # General error function. Simple enough, plug in msg, output error + help txt.
    print(f'Error: {msg}')
    print(a.helptxt)
    input('Press enter to exit...')
    quit()

def get_sett(arg, expected, allowmissing = False):
    # Attempts to get the setting
    if arg not in sys.argv: 
        KeyError(
        f'"{arg}" not present in "sys.argv"!'
    )
    try:
        val = sys.argv[sys.argv.index(arg) + 1]
    except IndexError: # If arg is at the end of the list
        if allowmissing:
            return None # We already know theres no argument after, no need to go any further
        panic(f'No value provided for argument {arg}')
    if val[:1] == '-': 
        if not allowmissing: panic(f'Invalid argument provided for {arg}: {val} Expected: {expected}')
        return None
    # Could break if a folder name begins with a dash. || TODO: Change to where 
    # all supported args are in a list, and this compares the setting to that list. 
    # Also could then use similar logic to check if there are any unsupported args
    return val                                                                                   
def test_path(arg, expected, allowmissing = False):                                                                    

    val = get_sett(arg = arg, expected = expected)
    path = Path(val)
    if Path.is_file(path) or allowmissing == True: return val # Returning string and not path object to not break existing logic for JSON saving and loading
    panic(f'Invalid argument provided for {arg}: {val} Expected: {expected}')

def cli_sheet_test(listn, sheetn):
    try:
        test_sheet(listn, sheetn)
    except ValueError as ve:
        print(traceback.format_exc())
        panic(f'ValueError: {ve}')
