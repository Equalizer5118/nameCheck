from PySide6.QtWidgets import (QMainWindow, QToolBar, QStatusBar,
                               QFileDialog, QMessageBox, QPushButton,
                               QProgressBar)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from qt_defwidget import DefWindow
from debugprint import p
from json_loading import *
from sys import argv
from os import startfile
from nameCheck import *
from qt_univerr import funcerror
import traceback
def echo():
    print('qt_mainwindow present')

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.adv = 0

        self.setFixedWidth(675)
        self.setFixedHeight(300)

        self.setWindowTitle("nameCheck")
        self.setWindowIcon(QIcon('_internal\\assets\\icon.ico')) # This won't work in dev testing, but it does in build

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.setStatusTip('General file actions')
        config_menu = file_menu.addMenu('Config...')
        config_menu.setStatusTip('Save or load current config')

        save_menu = config_menu.addMenu('Save...')

        save_default = save_menu.addAction("Save")
        save_default.triggered.connect(self.save_config_default)
        save_default.setStatusTip('Save the current config as default ("default.json")')

        save_as = save_menu.addAction('As...')
        save_as.triggered.connect(self.save_config)
        save_as.setStatusTip('Save the current config into a different file')

        load_menu = config_menu.addMenu('Load...')

        load_default = load_menu.addAction("Default")
        load_default.triggered.connect(self.load_config_default)
        load_default.setStatusTip('Load the default config ("default.json")')

        load_file = load_menu.addAction('JSON file...')
        load_file.triggered.connect(self.load_config)
        load_file.setStatusTip('Load the current config into a different file')

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
        toolbar.addAction(save_default)
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
        
    def save_config_default(self):
        name = 'default.json'
        self.statusBar().showMessage(export_json(name), 5000)
    
    def save_config(self):
        name = QFileDialog.getSaveFileName(caption='Save config as...', filter="JSON Files (*.json)")
        p(name)
        self.statusBar().showMessage(export_json(name[0]), 5000)
    
    def updatemenus(self):
        self.central_widget.configupdate()

    def load_config_default(self):
        name = 'default.json'
        p('Loading default.json')
        self.statusBar().showMessage(import_json(name), 5000)
        self.updatemenus()

    def load_config(self):
        p('Loading from selected json')
        diag = QFileDialog(self)
        diag.setNameFilter('JSON files (*.json)')
        diag.setFileMode(QFileDialog.ExistingFile)
        if diag.exec():
            name = diag.selectedFiles()
            self.statusBar().showMessage(import_json(name[0]), 5000)
        self.updatemenus()

    def help_button(self):
        try:
            startfile('README.md')
        except:
            funcerror('README.md does not exist!')
            return
        self.statusBar().showMessage('Opening README file in default editor...', 5000)

    def version_button(self):
        try:
            startfile('VERSION.md')
        except:
            funcerror('VERSION.md does not exist!')
            return
        self.statusBar().showMessage('Opening VERSION file in default editor...', 5000)

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
                self.progress_bar.setValue(0)
                checkNames1()
                self.progress_bar.setValue(1)
                checkNames2()
                self.progress_bar.setValue(2)
                results = checkNames3()
                self.progress_bar.setValue(3)
                msgbox = QMessageBox(icon=QMessageBox.Information)
                msgbox.setText(results)
                msgbox.setWindowTitle('Information')
                msgbox.exec()  
            except BaseException as e:
                traceback.print_tb(e.__traceback__)
                print(f'Exception: {e}')

                funcerror(f'An error occured! Error: \n {e}')

                ''' again, we are accepting every exception. why????
                    Well here, its a bit different. If there is an exception, I want the function to stop.
                    however, I also want to report the exception to the user for debugging purposes.
                    thats why I except every error then put it in a qt popup, so its easier to digest for the user.
                    the full trace still gets put in console, but the user can understand what the error was.
                '''
    
    def adv_togg(self):
        if self.adv == 0:
            self.adv = 1
            self.central_widget.showadvwindows()
            self.setFixedHeight(530)
        else:
            self.adv = 0
            self.central_widget.hideadvwindows()
            self.setFixedHeight(300)

    def quit_app(self):
        print('quit triggered!')
        self.app.quit()