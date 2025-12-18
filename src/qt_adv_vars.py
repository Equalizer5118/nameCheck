from datetime import datetime as dt
from pathlib import Path as path
from ver import ver

# This file is used to store variables outside of any function or file, so they can be accessed globally via import
# ========== VARIABLES SAVED TO JSON ==========

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
pg_gradecos = 'Sheet' # cos stands for "column or sheet". I have forgotten what this does so many times...
pg_gradesep = ''
pg_gradesepv = ''

# PG sheet adv values
yba_lastcol = 'Last Name'
yba_firstcol = 'First Name'
yba_gradecos = 'Sheet'
yba_gradesep = ''
yba_gradesepv = ''

taggedcol = 'Used on Page(s)' # Unused? Should be same on sheets directly exported from YBA
dontshowdupe = 0

# ========== VARIABLES NOT SAVED ==========

# These are generaly temporary variables not saved to JSON, but still used in here to be accessed globally

unac = []
noimg = []
verified = []
pgs = []
ybas = []
dat = dt.now()
logfile = path('log.txt')
openjson = None
log = ''
pglist = ''
ybalist = ''
pgi = ''
ybai = ''
pgmid = ''
namesim = []
debug = 0

method = 'gui' # Specifies if running in gui or cli mode

# Doesn't need to be changed or saved, but its useful to have here to avoid duplicate code
helptxt = f'''NameCheck version {ver}
Help Menu

Commands
    cli -                         Runs nameCheck in CLI mode
    (no commands) -               Runs nameCheck in GUI mode (most user friendly)
    
Options
    --version / -v -              Prints the version of nameCheck into console, then exits.
    --debug / -d -                Enables debug mode, which prints more info text into console
    --help / -help -              Shows this help menu

    CLI Options:
        Manual mode:
            --ybalist [path] -        Sets the path to the YBA coverage report spreadsheet file
            --ybacsheet [name] -      Sets the sheet name to read from in the YBA coverage report spreadsheet
            --pglist [path] -         Sets the path to the school roster spreadsheet file
            --pgcsheet [name] -       Sets the sheet name to read from in the school roster spreadsheet
            --nolog -                 Disables log file generation

            --savejson [name] -       Saves the current options to a json file with the given name. If no path is given, saves to 'data/[name].json'

        JSON mode:
            --json [path] -           Specifies a json file to load preset options from (overrides other CLI options). If no path given, saves to 'data/default.json'


'''