from datetime import datetime as dt
from pathlib import Path as path

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

# ========== VARIABLES NOT SAVED ==========

unac = []
noimg = []
verified = []
pgs = []
ybas = []
dat = dt.now()
logfile = path('log.txt')
log = ''
pglist = ''
ybalist = ''
pgi = ''
ybai = ''
namesim = []
