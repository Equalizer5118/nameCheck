import pandas as pd
from qt_univerr import funcerror
def echo():
    print('nameCheck present')
def init_pg(pgclist, pgcsheet):
# try:
   pglist = pd.read_excel(pgclist, pgcsheet)
   return pglist
# except OSError:
#   print(f'!!!!Path to for pg roster invalid or missing! Path given: {pgclist}')
#   funcerror('Invalid HS roster path given!')
#   raise OSError
# except ValueError:
#   print(f'!!!!Sheet name for pg roster invalid or missing in config file! Sheet name given: {pgcsheet}')
#   input("Press enter to exit the program...")
#   exit()
# except:
#   print('Something has gone wrong with the PG list loading and the program had to exit. Please check your config file and try again.')
#   print(f'List value: {pgclist}')
#   print(f'Sheet value: {pgcsheet}')
#   input("Press enter to exit...")
#   exit()

def init_yba(ybaclist, ybacsheet):
# try:
   ybalist = pd.read_excel(ybaclist, sheet_name=ybacsheet)
   return ybalist
# except OSError:
#   print(f'!!!!Path to for YBA roster invalid or missing in config file! Path given: {ybaclist}')
#   input("Press enter to exit the program...")
#   exit()
# except ValueError:
#   print(f'!!!!Sheet name for YBA roster invalid or missing in config file! Sheet name given: {ybacsheet}')
#   input("Press enter to exit the program...")
#   exit()
# except:
#   print('Something has gone wrong with the YBA list loading and the program had to exit. Please check your config file and try again.')
#   print(f'List value: {ybaclist}')
#   print(f'Sheet value: {ybacsheet}')
#   input("Press enter to exit...")
#   exit()
