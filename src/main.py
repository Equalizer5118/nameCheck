import traceback
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QSize
import sys
from pathlib import Path
try:
    from qt_mainwindow import DefWindow
    from debugprint import p
    from qt_adv_vars import export_json
except KeyError as ke:
    print(f'Full Trace + Error:')
    traceback.print_tb(ke.__traceback__)
    print(f'KeyError: {ke}')
    print('\n \n Malformed JSON file! \n \n')
    input('Press enter to rebuild JSON file and continue with the program...')
    print('Deleting "default.json"')
    Path.unlink(Path('default.json'))
    print('json deleted! reloading modules...')
    try:
        from qt_mainwindow import DefWindow
        from debugprint import p
        from qt_adv_vars import export_json
    except Exception as e:
        # s#### f#####d
        print('There was an error importing the required modules. One or more are missing/broken. Full exception: ')
        traceback.print_tb(e.__traceback__)
        print(f'Exception: {e}')
except Exception as e:
    # s#### f#####d
    print('There was an error importing the required modules. One or more are missing/broken. Full exception: ')
    traceback.print_tb(e.__traceback__)
    print(f'Exception: {e}')
finally:
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
app = QApplication(sys.argv)
window = DefWindow()
window.show()
#window.setFixedSize(QSize(165, 250))

app.exec()

p('GUI closed, saving default.json...')
export_json('default')
