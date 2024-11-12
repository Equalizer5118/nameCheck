from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QSize
from qt_mainwindow import DefWindow
import sys

app = QApplication(sys.argv)

window = DefWindow()
window.show()
#window.setFixedSize(QSize(165, 250))

app.exec()