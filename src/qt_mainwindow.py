from PySide6.QtWidgets import (QMessageBox, QLineEdit, QLabel, QGroupBox, 
                               QFileDialog, QWidget, QPushButton, QHBoxLayout, 
                               QVBoxLayout, QCheckBox)
from nameCheck import checkNames
from debugprint import p
from qt_univerr import funcerror
from sys import argv
import traceback
class DefWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pgclist = ''
        self.ybaclist = ''
        self.pgcsheet = ''
        self.ybacsheet = ''
        self.genlog = False

        self.setWindowTitle("nameCheck")

        
        groupbox = QGroupBox('nameCheck')

        #1st button
        button1label = QLabel(self)
        button1label.setText('Open HS roster')
        button1 = QPushButton("Open")
        button1.clicked.connect(self.button1_clicked)
        self.b1tbox = QLineEdit()
        self.b1tbox.setPlaceholderText('Path to HS roster')
        self.b1tbox.alignment()
        self.b1tbox.textChanged.connect(self.b1tbox_changed)
        self.b1sbox = QLineEdit()
        self.b1sbox.setPlaceholderText('Sheet name')
        self.b1sbox.alignment()
        self.b1sbox.textChanged.connect(self.b1sbox_changed)
        self.b1sbox.setFixedWidth(85)

        #1st button layout
        b1layout = QHBoxLayout()
        b1layout.addWidget(button1)
        b1layout.addWidget(self.b1tbox)
        b1layout.addWidget(self.b1sbox)

        #2nd button
        Button2label = QLabel(self)
        Button2label.setText('Open YBA covrep')
        button2 = QPushButton("Open")
        button2.clicked.connect(self.button2_clicked)
        self.b2tbox = QLineEdit()
        self.b2tbox.setPlaceholderText('Path to YBA roster')
        self.b2tbox.alignment()
        self.b2tbox.textChanged.connect(self.b2tbox_changed)
        self.b2sbox = QLineEdit()
        self.b2sbox.setPlaceholderText('Sheet name')
        self.b2sbox.alignment()
        self.b2sbox.textChanged.connect(self.b2sbox_changed)
        self.b2sbox.setFixedWidth(85)

        #2nd button layout
        b2layout = QHBoxLayout()
        b2layout.addWidget(button2)
        b2layout.addWidget(self.b2tbox)
        b2layout.addWidget(self.b2sbox)

        #log button
        logbutton = QCheckBox('Generate Log file', self)
        logbutton.stateChanged.connect(self.logbuttonclicked)

        #go button
        gobutton = QPushButton("Go!")
        gobutton.clicked.connect(self.gobutton_clicked)
        
        #final layout
        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(button1label)
        buttonlayout.addLayout(b1layout)
        buttonlayout.addWidget(Button2label)
        buttonlayout.addLayout(b2layout)
        buttonlayout.addWidget(logbutton)
        buttonlayout.addWidget(gobutton)

        groupbox.setLayout(buttonlayout)

        layout_master = QVBoxLayout(self)
        layout_master.addWidget(groupbox)
        self.setLayout(layout_master)

    def button1_clicked(self):
        pgclistt = QFileDialog.getOpenFileName(self, 'Open HS roster', '.', 'Excel Spreadsheets (*.xls *.xlsx)')
        p(str(pgclistt))
        liststart = str(pgclistt).find("'")
        listend = str(pgclistt)[liststart+1:].find("'")+liststart+1
        p(liststart)
        p(listend)
        pgclistt = str(pgclistt)[liststart+1:listend]
        p(pgclistt)
        self.b1tbox.setText(pgclistt)

    def button2_clicked(self):
        ybaclistt = QFileDialog.getOpenFileName(self, 'Open YBA roster', '.', 'Excel Spreadsheets (*.xls *.xlsx)')
        p(str(ybaclistt))
        liststart = str(ybaclistt).find("'")
        listend = str(ybaclistt)[liststart+1:].find("'")+liststart+1
        p(liststart)
        p(listend)
        ybaclistt = str(ybaclistt)[liststart+1:listend]
        p(ybaclistt)
        self.b2tbox.setText(ybaclistt)
    
    def logbuttonclicked(self, state):
        self.genlog = state
        if self.genlog == 2: self.genlog = True
        else: self.genlog = False
        p(f'toggle set to {self.genlog}')

    def b1tbox_changed(self, data):
        p(f'tbox1 set to {data}')
        self.pgclist = data

    def b2tbox_changed(self, data):
        p(f'tbox2 set to {data}')
        self.ybaclist = data

    def b1sbox_changed(self, data):
        p(f'sbox1 set to {data}')
        self.pgcsheet = data

    def b2sbox_changed(self, data):
        p(f'sbox2 set to {data}')
        self.ybacsheet = data

    def gobutton_clicked(self):
        if self.pgclist == '' or self.ybaclist == '' or self.ybacsheet == '' or self.ybacsheet == '':
            msgbox = QMessageBox(icon=QMessageBox.Information)
#            msgbox.setInformativeText('Paths mising!')
            msgbox.setText('One or more of the spreadsheet paths/sheet names are missing. Please set these values before continuing!')
            msgbox.setWindowTitle('Information')
            msgbox.exec()
        else: 
            p('All reqs satisfied, proceeding!')
            try: 
                results = checkNames(self.pgclist, self.pgcsheet, self.ybaclist, self.ybacsheet, self.genlog)
                msgbox = QMessageBox(icon=QMessageBox.Information)
                msgbox.setText(results)
                msgbox.setWindowTitle('Information')
                msgbox.exec()  
            except Exception as e:
                if '--debug' in argv or '-d' in argv: traceback.print_tb(e.__traceback__), print(f'Exception: {e}')
                funcerror(f'An error occured! Error: \n {e}')
        

'''
from PySide6.QtWidgets import QWidget, QCheckBox, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QFileDialog

class SelectWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('nameCheck')
#        groupbox = QGroupBox('Import Sheets')
        test = QCheckBox('Check Me!')

#        dialog1 = QFileDialog(self)
#        dialog1.setNameFilter('Excel Spreadsheets (*.xls *.xlsx)')
        
#        dialog2 = QFileDialog(self)
#        dialog2.setNameFilter('Excel Spreadsheets (*.xls *.xlsx)')

#        dialog1.fileSelected.connect(self.dialog1_set)

        layout = QVBoxLayout()
        layout.addWidget(test)
#        layout.addWidget(dialog1)
#        layout.addWidget(dialog2)

        self.setLayout(layout)

    def dialog1_set(data):
        p(f'List set! Data: {data}')
        pgclist = data
'''