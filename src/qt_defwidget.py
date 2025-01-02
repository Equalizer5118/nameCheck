from PySide6.QtWidgets import (QLineEdit, QLabel, QGroupBox, 
                               QFileDialog, QWidget, QPushButton, QHBoxLayout, 
                               QVBoxLayout, QCheckBox)
from PySide6.QtCore import Qt
from debugprint import p
from qt_advwindow import QPgAdvWindow, QYbaAdvWindow
import qt_adv_vars as a

class DefWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ================= Left Group Box =================
        groupbox = QGroupBox('nameCheck')

        #1st button
        button1label = QLabel(self)
        button1label.setText('Open HS roster')
        button1 = QPushButton("Open")
        button1.setStatusTip('Open an excel file...')
        button1.clicked.connect(self.button1_clicked)
        self.b1tbox = QLineEdit()
        self.b1tbox.setPlaceholderText('Path to HS roster')
        self.b1tbox.setStatusTip('Path to excel file with School roster')
        self.b1tbox.alignment()
        self.b1tbox.textChanged.connect(self.b1tbox_changed)
        self.b1tbox.setText(a.pgclist)
        self.b1sbox = QLineEdit()
        self.b1sbox.setPlaceholderText('Sheet name')
        self.b1sbox.setStatusTip('Sheet name to find all the names')
        self.b1sbox.alignment()
        self.b1sbox.textChanged.connect(self.b1sbox_changed)
        self.b1sbox.setText(a.pgcsheet)
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
        button2.setStatusTip('Open an excel file...')
        self.b2tbox = QLineEdit()
        self.b2tbox.setPlaceholderText('Path to YBA roster')
        self.b2tbox.setStatusTip('Path to excel file with YBA covrep')
        self.b2tbox.alignment()
        self.b2tbox.textChanged.connect(self.b2tbox_changed)
        self.b2tbox.setText(a.ybaclist)
        self.b2sbox = QLineEdit()
        self.b2sbox.setPlaceholderText('Sheet name')
        self.b2sbox.setStatusTip('Sheet name to find all the names')
        self.b2sbox.alignment()
        self.b2sbox.textChanged.connect(self.b2sbox_changed)
        self.b2sbox.setText(a.ybacsheet)
        self.b2sbox.setFixedWidth(85)

        #2nd button layout
        b2layout = QHBoxLayout()
        b2layout.addWidget(button2)
        b2layout.addWidget(self.b2tbox)
        b2layout.addWidget(self.b2sbox)

        #log button
        self.logbutton = QCheckBox('Generate Log file', self)
        if a.genlog == True: 
            self.logbutton.setCheckState(Qt.Checked)
        self.logbutton.stateChanged.connect(self.logbuttonclicked)

        #final layout
        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(button1label)
        buttonlayout.addLayout(b1layout)
        buttonlayout.addWidget(Button2label)
        buttonlayout.addLayout(b2layout)
        buttonlayout.addWidget(self.logbutton)

        groupbox.setLayout(buttonlayout)
        groupbox.setFixedHeight(200)
        groupbox.setFixedWidth(400)
        groupbox.setAlignment(Qt.AlignTop)
        groupboxl = QVBoxLayout()
        groupboxl.addWidget(groupbox)
        groupboxl.setAlignment(Qt.AlignTop)
        # ===================================================

        # ================= Right group Box =================

        self.pgadv = QPgAdvWindow()

        self.ybaadv = QYbaAdvWindow()

        rgroupboxl = QVBoxLayout(self)
        rgroupboxl.addWidget(self.pgadv)
        rgroupboxl.addWidget(self.ybaadv)

        self.rgroupbox = QGroupBox('Advanced Menus')
        self.rgroupbox.setLayout(rgroupboxl)
        self.rgroupbox.hide()
        
        # ===================================================

        layout_master = QHBoxLayout(self)
        layout_master.setAlignment(Qt.AlignHCenter)
        layout_master.addLayout(groupboxl)
        layout_master.addWidget(self.rgroupbox)
        self.setLayout(layout_master)

    def configupdate(self):
        self.b1tbox.setText(a.pgclist)
        self.b2sbox.setText(a.pgcsheet)
        self.b2tbox.setText(a.ybaclist)
        self.b2sbox.setText(a.ybacsheet)
        if a.genlog == True: 
            self.logbutton.setCheckState(Qt.Checked)
        else:
            self.logbutton.setCheckState(Qt.Unchecked)
        self.pgadv.configchange()
        self.ybaadv.configchange()
        

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

    def showadvwindows(self):
        self.rgroupbox.show()

    def hideadvwindows(self):
        self.rgroupbox.hide()
