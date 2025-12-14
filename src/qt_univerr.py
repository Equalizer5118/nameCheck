from PySide6.QtWidgets import QMessageBox
def echo():
    print('nameCheck present')
def funcerror(reason):
    msgbox = notice(title='Action Failed!', reason=reason, icon=QMessageBox.Critical)
    msgbox.exec()

def notice(title = 'Information', reason = '', icon = QMessageBox.Information):
    msgbox = QMessageBox(icon=icon)
    msgbox.setWindowTitle(title)
    msgbox.setText(reason)
    return msgbox