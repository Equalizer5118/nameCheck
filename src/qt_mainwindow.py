from PySide6.QtWidgets import (QMessageBox, QLineEdit, QLabel, QGroupBox, 
                               QFileDialog, QWidget, QPushButton, QHBoxLayout, 
                               QVBoxLayout, QCheckBox)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from nameCheck import checkNames
from debugprint import p
from qt_univerr import funcerror
from qt_advwindow import advwindow
import qt_adv_vars as a
from sys import argv
import traceback
def echo():
    print('qt_mainwindow present')
class DefWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("nameCheck")
        self.setWindowIcon(QIcon('_internal\\assets\\icon.ico')) # This won't work for testing, but it does in build

        
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
        self.b1tbox.setText(a.pgclist)
        self.b1sbox = QLineEdit()
        self.b1sbox.setPlaceholderText('Sheet name')
        self.b1sbox.alignment()
        self.b1sbox.textChanged.connect(self.b1sbox_changed)
        self.b1sbox.setText(a.pgcsheet)
        self.b1sbox.setFixedWidth(85)
        b1adv = QPushButton("Advanced...")
        b1adv.clicked.connect(self.b1adv_clicked)

        #1st button layout
        b1layout = QHBoxLayout()
        b1layout.addWidget(button1)
        b1layout.addWidget(self.b1tbox)
        b1layout.addWidget(self.b1sbox)
        b1layout.addWidget(b1adv)

        #2nd button
        Button2label = QLabel(self)
        Button2label.setText('Open YBA covrep')
        button2 = QPushButton("Open")
        button2.clicked.connect(self.button2_clicked)
        self.b2tbox = QLineEdit()
        self.b2tbox.setPlaceholderText('Path to YBA roster')
        self.b2tbox.alignment()
        self.b2tbox.textChanged.connect(self.b2tbox_changed)
        self.b2tbox.setText(a.ybaclist)
        self.b2sbox = QLineEdit()
        self.b2sbox.setPlaceholderText('Sheet name')
        self.b2sbox.alignment()
        self.b2sbox.textChanged.connect(self.b2sbox_changed)
        self.b2sbox.setText(a.ybacsheet)
        self.b2sbox.setFixedWidth(85)
        b2adv = QPushButton("Advanced...")
        b2adv.clicked.connect(self.b2adv_clicked)

        #2nd button layout
        b2layout = QHBoxLayout()
        b2layout.addWidget(button2)
        b2layout.addWidget(self.b2tbox)
        b2layout.addWidget(self.b2sbox)
        b2layout.addWidget(b2adv)

        #log button
        logbutton = QCheckBox('Generate Log file', self)
        if a.genlog == True: 
            logbutton.setCheckState(Qt.Checked)
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

    def b1adv_clicked(self):
        a.pg_or_yba = 'pg'
        advwin = advwindow()
        advwin.exec()

    def b2adv_clicked(self):
        a.pg_or_yba = 'yba'
        advwin = advwindow()
        advwin.exec()

    def button1_clicked(self):
        pgclistd = QFileDialog(self)
        pgclistd.directoryEntered.connect(self.setlastdir)
        pgclistd.setFileMode(QFileDialog.ExistingFile)
        pgclistd.setNameFilter('Excel Spreadsheets (*.xls *.xlsx)')
        pgclistd.setDirectory(a.last_dir)
        pgclistt = ''
        if pgclistd.exec():
            pgclistt = pgclistd.selectedFiles()
        p(str(pgclistt))
        liststart = str(pgclistt).find("'")
        listend = str(pgclistt)[liststart+1:].find("'")+liststart+1
        p(liststart)
        p(listend)
        pgclistt = str(pgclistt)[liststart+1:listend]
        p(pgclistt)
        self.b1tbox.setText(pgclistt)

    def button2_clicked(self):
        ybaclistd = QFileDialog(self)
        ybaclistd.directoryEntered.connect(self.setlastdir)
        ybaclistd.setFileMode(QFileDialog.ExistingFile)
        ybaclistd.setNameFilter('Excel Spreadsheets (*.xls *.xlsx)')
        ybaclistd.setDirectory(a.last_dir)
        ybaclistt = ''
        if ybaclistd.exec():
            ybaclistt = ybaclistd.selectedFiles()
#        ybaclistt.getOpenFileName(self, 'Open YBA roster', a.last_dir, 'Excel Spreadsheets (*.xls *.xlsx)')
        
        p(str(ybaclistt))
        liststart = str(ybaclistt).find("'")
        listend = str(ybaclistt)[liststart+1:].find("'")+liststart+1
        p(liststart)
        p(listend)
        ybaclistt = str(ybaclistt)[liststart+1:listend]
        p(ybaclistt)
        self.b2tbox.setText(ybaclistt)

    def setlastdir(self, data):
        p(f'Last dir: {data}')
        a.last_dir = data
    
    def logbuttonclicked(self, state):
        a.genlog = state
        if a.genlog == 2: 
            a.genlog = True
        else: 
            a.genlog = False
        p(f'toggle set to {a.genlog}')

    def b1tbox_changed(self, data):
        p(f'tbox1 set to {data}')
        a.pgclist = data

    def b2tbox_changed(self, data):
        p(f'tbox2 set to {data}')
        a.ybaclist = data

    def b1sbox_changed(self, data):
        p(f'sbox1 set to {data}')
        a.pgcsheet = data

    def b2sbox_changed(self, data):
        p(f'sbox2 set to {data}')
        a.ybacsheet = data

    def gobutton_clicked(self):
        if a.pgclist == '' or a.ybaclist == '' or a.pgcsheet == '' or a.ybacsheet == '':
            msgbox = QMessageBox(icon=QMessageBox.Information)
#            msgbox.setInformativeText('Paths mising!')
            msgbox.setText('One or more of the spreadsheet paths/sheet names are missing. Please set these values before continuing!')
            msgbox.setWindowTitle('Information')
            msgbox.exec()
        else: 
            p('All reqs satisfied, proceeding!')
            try: 
                results = checkNames()
                msgbox = QMessageBox(icon=QMessageBox.Information)
                msgbox.setText(results)
                msgbox.setWindowTitle('Information')
                msgbox.exec()  
            except Exception as e:
                traceback.print_tb(e.__traceback__)
                print(f'Exception: {e}')

                funcerror(f'An error occured! Error: \n {e}')
                ''' again, we are accepting every exception. why????
                    Well here, its a bit different. If there is an exception, I want the function to stop
                    however, I also want to report the exception to the user for debugging purposes
                    thats why I except every error then put it in a qt popup, so its easier to digest for the user
                    the full trace still gets put in console, but the user can understand what the error was.
                '''
