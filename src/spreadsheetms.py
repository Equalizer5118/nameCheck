import pandas as pd
from debugprint import p
def echo():
    print('nameCheck present')
def init_sheet(list, pgcsheet, engine = 'openpyxl'):
   p(list[-3:])
   if list[-3:] == 'ods': engine = 'odf'
   rlist = pd.read_excel(list, pgcsheet, engine=engine)
   return rlist