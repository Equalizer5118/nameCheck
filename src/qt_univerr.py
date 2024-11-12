from PySide6.QtWidgets import QMessageBox
def funcerror(reason):
    msgbox = QMessageBox(icon=QMessageBox.Critical)
#        msgbox.setInformativeText('Paths mising!')
    msgbox.setText(reason)
    msgbox.setWindowTitle('nameCheck Failed!')
    msgbox.exec()