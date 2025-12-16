# GUI initialization script. This contians the main GUI loop and error catching for module imports/JSON loading.
import traceback
import sys
from PySide6.QtWidgets import QApplication
from pathlib import Path
import os

def panic(e):
    # This function is a template for when an exception occurs during module imports
    # AKA Its still broken for some damn reason...
    print('There was an error importing the required modules. One or more are missing/broken. Full exception: ')
    traceback.print_tb(e.__traceback__)
    print(f'Exception: {e}')
    input('Press enter to close the program...')
    exit()
def run():
    loaded = False
    while not loaded: loaded = loadmod()
    setup()

def loadmod():
    # Ensure data path exists

    if not Path('data').is_dir():
        p('Data path does not exist, creating...')
        os.makedirs('data')

    # Try to import main modules and load JSON settings
    try:
        from qt_mainwindow import MainWindow
        from debugprint import p
        from json_loading import import_json
        import_json('data/default.json')
    except KeyError as ke:
        #'''
        # This catches any errors with loading the json file. The logic for checking if it exists below,
        # so this only catches if a key is missing. It will then delete the json, which will be recreated on program exit
        #'''
        print(f'Full Trace + Error:')
        traceback.print_tb(ke.__traceback__)
        print(f'KeyError: {ke}')
        print('===============\n===============\n==Malformed JSON file!\n===============\n===============')
        input('Press enter to rebuild JSON file and continue with the program\nTHIS WILL DELETE YOUR STORED SETTINGS. If you want to copy your settings before they are deleted, do so now.\nPress enter to continue...')
        print('Deleting "data/default.json"')
        Path.unlink(Path('data/default.json'))
        print('json deleted! Trying to reload modules...')
        return False
    except BaseException as e:
        # We don't know what happened, but its broken.
        panic(e)
    p('Modules imported')
    return True
    '''
    You might rightfully be asking "Equal, why are you catching every exception? Isnt that a bad practice?"
    and normally, yeah, it is. The problem is that my school computers won't let us open up CMD.
    My home PC does, but my school desktop doesn't. As such, if an exception occurs at school during the 
    initial window setup, the console closes immediately and I cant see the error. So, I made this little
    script, which will catch every error and then display it in the console. That way, 
    I can actually see the error instead of having to guess at what died.

    Basically, screw you school district.
    '''

def setup():
    from qt_mainwindow import MainWindow
    from debugprint import p
    from json_loading import export_json   

    # Set up application
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()

    app.exec()
    p('GUI closed, saving default.json...')
    export_json('data/default.json')
    p('json successfully saved!')
    return 'GUI completed'