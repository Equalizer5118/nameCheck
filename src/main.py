import sys
if '--version' in sys.argv or '-v' in sys.argv:
    from ver import ver
    print(f'nameCheck version: {ver}')
    input('Press enter to close the program...')
    quit()
if '--debug' in sys.argv or '-d' in sys.argv:
    import qt_adv_vars as a
    a.debug = 1
    
import traceback
from PySide6.QtWidgets import QApplication
from pathlib import Path
import os
try:
    from qt_mainwindow import MainWindow
    from debugprint import p
    from json_loading import *
except KeyError as ke:
    '''
    This catches any errors with loading the json file. The logic for checking if it exists is in qt_adv_vars,
    so this only catches if a key is missing. It will then delete the json, which will be saved on program exit
    '''
    print(f'Full Trace + Error:')
    traceback.print_tb(ke.__traceback__)
    print(f'KeyError: {ke}')
    print('\n \n Malformed JSON file! \n \n')
    input('Press enter to rebuild JSON file and continue with the program...')
    print('Deleting "default.json"')
    Path.unlink(Path('default.json'))
    print('json deleted! reloading modules...')
    try:
        from qt_mainwindow import MainWindow
        from debugprint import p
        from qt_adv_vars import export_json
    except BaseException as e:
        # Its still broken for some damn reason...
        print('There was an error importing the required modules. One or more are missing/broken. Full exception: ')
        traceback.print_tb(e.__traceback__)
        print(f'Exception: {e}')
        input('Press enter to close the program...')
        exit()
except BaseException as e:
    # s#### f#####d
    print('There was an error importing the required modules. One or more are missing/broken. Full exception: ')
    traceback.print_tb(e.__traceback__)
    print(f'Exception: {e}')
    input('Press enter to close the program...')
    exit()

'''
You might rightfully be asking "Equal, why are you catching every exception? Isnt that a bad practice?"
and normally, yeah, it is. The problem is that my school computers won't let us open up CMD.
My home PC does, but my school desktop doesn't. As such, if an exception occurs at school during the 
initial window setup, the console closes immediately and I cant see the error. So, I made this little
script, which will catch every error and then display it in the console. That way, 
I can actually see the error instead of having to guess at what died.

Basically, screw you school district.
'''
if Path('data').is_dir() == False:
    p('Data path does not exist, creating...')
    os.makedirs('data')
if Path(os.path.abspath('data\\default.json')).is_file():
    import_json('data\\default.json')
app = QApplication(sys.argv)
window = MainWindow(app)
window.show()

app.exec()

p('GUI closed, saving default.json...')
export_json('data\\default.json')
p('json successfully saved!')