from PySide6.QtWidgets import QMessageBox
def echo():
    print('nameCheck present')
def funcerror(reason):
    msgbox = QMessageBox(icon=QMessageBox.Critical)
    msgbox.setText(reason)
    msgbox.setWindowTitle('Action Failed!')
    msgbox.exec()