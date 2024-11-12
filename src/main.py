from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QSize
from qt_mainwindow import DefWindow
import nameCheck
import spreadsheetms
import qt_univerr
import writelog
import debugprint
import configcreate
import sys
nameCheck.echo()
qt_univerr.echo()
debugprint.echo()
configcreate.echo()
spreadsheetms.echo()
app = QApplication(sys.argv)

window = DefWindow()
window.show()
#window.setFixedSize(QSize(165, 250))

app.exec()