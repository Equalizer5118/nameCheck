# so i dont get warns
import configparser
from pathlib import Path as path
config = configparser.ConfigParser()

def init_config():
    if not path.exists(path('config.ini')): 
        create_config()
    else:
        print('Config found! Poceeding...')

def create_config():
    config['PATHS'] = {'pg_class_roster': 'path_to_PGlist_here', 'yba_class_covrep': 'path_to_yba_class_covrep'}
    config['SHEETNAMES'] = {'roster_sheet_name': '0', 'covrep_sheet_name': '0'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print('No config file found, created empty template. Please add paths to the spreadsheets in "config.ini" before proceeding!')
    k = input("")
    quit()