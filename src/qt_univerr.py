from PySide6.QtWidgets import QMessageBox, QCheckBox, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
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

def chkbox(boxtext = 'CheckBox', checked = False, desc = 'Description', connect = None):
    containerbox = QHBoxLayout()
    containerbox.setAlignment(Qt.AlignmentFlag.AlignTop)
    
    checkbox = QCheckBox()
    checkbox.setCheckState(checked)
    checkbox.setText(boxtext)
    checkbox.stateChanged.connect(connect)

    label = QLabel(text=desc)

    containerbox.addWidget(checkbox)
    containerbox.addWidget(label)
    return containerbox
    # Remember to add to layout with layout.addLayout(), as this function returns a layout not a widget