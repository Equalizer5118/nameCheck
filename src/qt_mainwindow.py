from PySide6.QtWidgets import (QMainWindow, QToolBar, QStatusBar,
                               QFileDialog, QMessageBox, QPushButton,
                               QProgressBar, QCheckBox, QDialog, 
                               QScrollArea, QGroupBox, QVBoxLayout)
from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QIcon
from qt_defwidget import DefWindow
from debugprint import p
from json_loading import *
import pyquark # Dear CodeWizard777 from random stackoverflow thread, I love you. Why is os.startfile windows only??????
from nameCheck import *
from qt_univerr import funcerror, notice, chkbox
import qt_adv_vars as a
import traceback
def echo():
    print('qt_mainwindow present')

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.ready = False
        self.app = app
        self.adv = False
        self.default_json = 'data/default.json'

        self.setFixedWidth(700)
        self.setFixedHeight(300)

        self.setWindowTitle("nameCheck")
        self.setWindowIcon(QIcon('_internal/assets/icon.ico')) # This won't work in dev testing, but it does in build

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.setStatusTip('General file actions')
        config_menu = file_menu.addMenu('Config...')
        config_menu.setStatusTip('Save or load current config')

        self.save_default = config_menu.addAction("Save")
        self.save_default.triggered.connect(self.save_config_default)
        self.save_default.setStatusTip(f'Save the current config as default ("{self.default_json}")')

        save_as = config_menu.addAction('Save As...')
        save_as.triggered.connect(self.save_config)
        save_as.setStatusTip('Save the current config into a different file')

        divider = config_menu.addSeparator()

        self.load_default = config_menu.addAction("Load Default")
        self.load_default.triggered.connect(self.load_config_base)
        self.load_default.setStatusTip(f'Load the default config ("{self.default_json}")')

        load_file = config_menu.addAction('Load JSON file...')
        load_file.triggered.connect(self.load_config)
        load_file.setStatusTip('Load the current config into a different file')

        preferences_action = file_menu.addAction('Preferences')
        preferences_action.triggered.connect(self.pref_clicked)

        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)
        quit_action.setStatusTip("Exits the program (duh)")

        window_menu = menu_bar.addMenu('Window')
        togg_adv = window_menu.addAction('Toggle Advanced Windows')
        togg_adv.triggered.connect(self.adv_togg)

        help_menu = menu_bar.addMenu('Help')
        help_action = help_menu.addAction('README.md')
        help_action.triggered.connect(self.help_button)
        help_action.setStatusTip('Opens the readme file (README.MD)')
        version_action = help_menu.addAction('Changelog')
        version_action.triggered.connect(self.version_button)
        version_action.setStatusTip('Opens the changelog file (VERSION.MD)')

        toolbar = QToolBar('Main Toolbar')
        toolbar.setMovable(0)
        toolbar.setFloatable(0)
        self.addToolBar(toolbar)
        toolbar.addAction(self.save_default)
        toolbar.addAction(togg_adv)

        #go button
        gobutton = QPushButton("Go!")
        gobutton.clicked.connect(self.gobutton_clicked)
        gobutton.setStatusTip('Run the comparing script')
        gobutton.setMinimumWidth(100)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(1)
        self.progress_bar.setMaximum(3)
        self.progress_bar.setMaximumWidth(300)
        self.progress_bar.setValue(3)

        self.central_widget = DefWindow()

        self.setCentralWidget(self.central_widget)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.setSizeGripEnabled(0)
        self.status_bar.addPermanentWidget(self.progress_bar)
        self.status_bar.addPermanentWidget(gobutton, 0.7)
        self.status_bar.reformat()
        self.ready = True
        
        # attempted fix for window size change on unfocus in Linux. || TODO: #2 Make this work
    '''    
    def focusInEvent(self, event):  
        p(self.size())
        if self.ready: 
            p("ready, checking size")
            self.check_size()
            p(self.size())
        return super().changeEvent(event)
    '''
    
    def save_config_default(self):
        name = self.default_json
        self.statusBar().showMessage(export_json(name), 5000)
    
    def pref_clicked(self):
        p('Preferences action clicked!')
        self.pref_window = Preferences(self.app)
        self.pref_window.show()
    
    def save_config(self):
        name = QFileDialog.getSaveFileName(caption='Save config as...', filter="JSON Files (*.json)")
        p(name)
        self.statusBar().showMessage(export_json(name[0]), 5000)
        self.default_json = name[0]
    
    def statusbar_message(self, message, timeout=5000):
        self.statusBar().showMessage(message, timeout)
        self.updatemenus()

    def updatemenus(self):
        self.central_widget.configupdate()

    def load_config_base(self, name = None):
        p(f'{name}. nametype:' + str(type(name)))
        if type(name) != str: name = self.default_json
        p(f'Loading "{name}"')
        res = json_load_GUI(name)
        if res[0] != 0:
            funcerror(f'Failed to load config from {name}.\nErrorCode{res[0]}: {res[1]}')
        else:
            self.statusbar_message(f'Loaded settings from {name}', 5000)


    def load_config(self):
        p('Loading from selected json')
        diag = QFileDialog(self)
        diag.setNameFilter('JSON files (*.json)')
        diag.setFileMode(QFileDialog.ExistingFile)
        if diag.exec():
            name = diag.selectedFiles()
            self.load_config_base(name)
            self.statusbar_message(f'Loaded settings from {name}', 5000)
        self.default_json = name[0]

    def help_button(self):
        try:
            pyquark.filestart('README.md')
        except:
            funcerror('README.md does not exist!')
            return
        self.statusBar().showMessage('Opening README file in default editor...', 5000)

    def version_button(self):
        try:
            pyquark.filestart('VERSION.md')
        except:
            funcerror('VERSION.md does not exist! HELP!')
            return
        self.statusBar().showMessage('Opening VERSION file in default editor...', 5000)

    def dont_show(self, state):
        a.dontshowdupe = state
        p(a.dontshowdupe)

    def gobutton_clicked(self):
        
        def go():
            self.progress_bar.setValue(0)
            checkNames1()
            self.progress_bar.setValue(1)
            checkNames2()
            self.progress_bar.setValue(2)
            results = checkNames3()
            self.progress_bar.setValue(3)
            p('Finished namecheck')
            msgbox = notice(reason = results)
            if a.log != '': msgbox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Open)
            ret = msgbox.exec()
            if ret == QMessageBox.StandardButton.Open:
                pyquark.filestart('log.txt')

        if a.pgclist == '' or a.ybaclist == '' or a.pgcsheet == '' or a.ybacsheet == '':
            msgbox = notice(reason='One or more of the spreadsheet paths/sheet names are missing. Please set these values before continuing!')
            msgbox.exec()
            return 1
        if a.pgclist == a.ybaclist and a.dontshowdupe != 2:
            p('Hold it!')
            msgbox = notice(reason='Spreadsheet paths are identical! Are you sure you want to proceed?')

            chkbox = QCheckBox()
            chkbox.setText('Do not show again')
            chkbox.stateChanged.connect(self.dont_show)

            msgbox.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
            msgbox.setCheckBox(chkbox)
            msgbox.setDefaultButton(QMessageBox.StandardButton.Yes)
            ret = msgbox.exec()
            if ret == QMessageBox.StandardButton.Yes:
                pass
            elif ret == QMessageBox.StandardButton.No:
                return 1
            else:
                return 1
        p('All reqs satisfied, proceeding!')
        if a.debug == 0: 
            try: 
                ret = go()
            except ValueError as ve:
                print(traceback.format_exc())
                funcerror(f'Sheet name does not exist! Error: \n{ve}')
            except FileNotFoundError as fnfe:
                print(traceback.format_exc())
                funcerror(f'File not found! Error: \n{fnfe}')
            except BaseException as e: # essentially functions the same as if BaseException was not handled, but gives the user an error window instead of just cryptic console text
                print(traceback.format_exc())
                funcerror(f'Unhandled Exception! Error: \n {e}')
        else:
            ret = go()

            

    ''' again, we are accepting every exception. why????
                    Well here, its a bit different. If there is an exception, I want the function to stop.
                    however, I also want to report the exception to the user for debugging purposes.
                    thats why I except every error then put it in a qt popup, so its easier to digest for the user, if its a them problem
                    the full trace still gets put in console, but the user can understand what the error was a little easier.
                    in theory.
    '''
    def check_size(self):
        p('check_size called')
        if self.adv:
            self.central_widget.showadvwindows()
            self.setFixedHeight(530)
            self.setMaximumHeight(530)
            self.setFixedSize(700, 530)
            p("Set Size 530")
        else:
            self.central_widget.hideadvwindows()
            self.setFixedHeight(300)
            self.setMaximumHeight(300)
            self.setFixedSize(700, 300)
            p("Set Size 300")
    def adv_togg(self):
        self.adv = not self.adv
        self.check_size()
        p(self.adv)
        p(self.size())

    def quit_app(self):
        print('quit triggered!')
        self.app.quit()

class Preferences(QDialog):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Preferences')
        self.setWindowIcon(QIcon('_internal/assets/icon.ico'))
        self.setFixedSize(603,103)

        # Dupe sheet warning checkbox
        if a.dontshowdupe == 2:
            dupechked = Qt.CheckState.Checked
        else:
            dupechked = Qt.CheckState.Unchecked
        showdupechk = chkbox('Do not show duplicate sheet warning', dupechked, 'If enabled, the program will not warn you \nif both spreadsheet paths are identical.', self.dupe_changed)
        
        # Inner layout
        Vlayout = QVBoxLayout()
        Vlayout.addLayout(showdupechk)

        # Outer layout
        groupbox = QGroupBox('Preferences')
        groupbox.setLayout(Vlayout)
        groupbox_layout = QVBoxLayout()
        groupbox_layout.addWidget(groupbox)
        self.setLayout(groupbox_layout)

    def dupe_changed(self, state):
        a.dontshowdupe = state
        p(a.dontshowdupe)
        
        
        