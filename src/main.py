#try:
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QSize
from qt_mainwindow import DefWindow
from debugprint import p
import qt_univerr
import sys
from qt_adv_vars import export_json
app = QApplication(sys.argv)
window = DefWindow()
window.show()
#window.setFixedSize(QSize(165, 250))

app.exec()

p('GUI closed, saving default.json...')
export_json('default')
'''
except Exception as e:
    # s###s f######
    try:
        print(e.__traceback__)
        qt_univerr.funcerror(f'Program failed to initialize! \n Error: {e} \n Please report this problem on the repo, with the full trace!')
    except:
        #oh its really bad, QT won't load. s###
        print(f'There was a critical error, likely to do with QT failing to initialize. Here is the full trace:')
        print(e.__traceback__)
        print(e)
        print('Please report this problem on the repo, with the full trace!')
        input('Press enter key to close...')
'''
'''
You might rightfully be asking "Equal, why are you catching every exception? Isnt that a bad practice?"
and normally, yeah, it is. The problem is that my school computers won't let us open up CMD windows.
My home PC does, but my school desktop doesn't. As such, if an exception occurs at school during the 
initial window setup, the console closes immediately and I cant see the error. So, I made this little
script, which will catch every error and then display it in the console and in a QT popup. That way, 
I can actually see the error instead of having to guess at what died.

Basically, screw you school district.
'''
