# TODO: Reduce duplicate code!
from PySide6.QtWidgets import (QWidget, QLineEdit, QHBoxLayout,
                                QGroupBox, QVBoxLayout, QComboBox, QLabel)
import qt_adv_vars as a
from debugprint import p
def echo(data):
    print('qt_advwindow present')
class QPgAdvWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        
        groupbox = QGroupBox('Roster Advanced Window')

        # last name box
        ln_lab = QLabel('Last Name column')
        self.ln_tbox = QLineEdit()
        self.ln_tbox.setText(a.pg_lastcol)
        self.ln_tbox.textChanged.connect(self.ln_tbox_var)

        ln_layout = QVBoxLayout()
        ln_layout.addWidget(ln_lab)
        ln_layout.addWidget(self.ln_tbox)

        # first name box
        fn_lab = QLabel('First Name column')
        self.fn_tbox = QLineEdit()
        self.fn_tbox.setText(a.pg_firstcol)
        self.fn_tbox.textChanged.connect(self.fn_tbox_var)

        fn_layout = QVBoxLayout()
        fn_layout.addWidget(fn_lab)
        fn_layout.addWidget(self.fn_tbox)

        glayout = QVBoxLayout()
        glayout.addLayout(ln_layout)
        glayout.addLayout(fn_layout)
        
        # dropdown
        divider_label = QLabel('Class Divider')
        self.divider_type = QComboBox()
        self.divider_type.addItem('Sheet')
        self.divider_type.addItem('Column')
        self.divider_type.currentIndexChanged.connect(self.dropdown_changed)
        self.divider_var = QLineEdit()
        self.divider_var.setFixedWidth(65)
        self.divider_var.textChanged.connect(self.var_changed)
        self.divider_var.setPlaceholderText('Column')
        self.divider_var_check = QLineEdit()
        self.divider_var_check.setFixedWidth(45)
        self.divider_var_check.textChanged.connect(self.var_check_changed)
        self.divider_var_check.setPlaceholderText('Val')
        self.divider_var.setText(a.pg_gradesep)
        self.divider_var_check.setText(a.pg_gradesepv)
        if a.pg_gradecos == 'Sheet':
            self.divider_type.setCurrentIndex(0)
            self.divider_var.hide()
            self.divider_var_check.hide()
        elif a.pg_gradecos == 'Column':
            self.divider_type.setCurrentIndex(1)

        div_sublayout = QHBoxLayout()
        div_sublayout.addWidget(self.divider_type)
        div_sublayout.addWidget(self.divider_var)
        div_sublayout.addWidget(self.divider_var_check)

        div_layout = QVBoxLayout()
        div_layout.addWidget(divider_label)
        div_layout.addLayout(div_sublayout)
        glayout.addLayout(div_layout)
        
        groupbox.setLayout(glayout)

        mlayout = QVBoxLayout(self)
        mlayout.addWidget(groupbox)
        self.setLayout(mlayout)

    def ln_tbox_var(self, data):
        a.pg_lastcol = data
        p(data)

    def fn_tbox_var(self, data):
        a.pg_firstcol = data
        p(data)
    
    def dropdown_changed(self, data):
        p(f'Dropdown Changed! {data}, {self.divider_type.currentText()}')
        a.pg_gradecos = self.divider_type.currentText()
        if data == 0: 
            self.divider_var.hide()
            self.divider_var_check.hide()
        else:
            self.divider_var.show()
            self.divider_var_check.show()

    def var_changed(self, data):
        p(f'Var changed, {data}')
        a.pg_gradesep = data

    def var_check_changed(self, data):
        p(f'Var_check changed, {data}')
        a.pg_gradesepv = data

    def configchange(self):
        self.ln_tbox.setText(a.pg_lastcol)
        self.fn_tbox.setText(a.pg_firstcol)
        self.divider_var.setText(a.pg_gradesep)
        self.divider_var_check.setText(a.pg_gradesepv)
        if a.pg_gradecos == 'Sheet':
            self.divider_type.setCurrentIndex(0)
            self.divider_var.hide()
            self.divider_var_check.hide()
        elif a.pg_gradecos == 'Column':
            self.divider_type.setCurrentIndex(1)

class QYbaAdvWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        
        groupbox = QGroupBox('Covrep Advanced Window')

        # last name box
        ln_lab = QLabel('Last Name column')
        self.ln_tbox = QLineEdit()
        self.ln_tbox.setText(a.yba_lastcol)
        self.ln_tbox.textChanged.connect(self.ln_tbox_var)

        ln_layout = QVBoxLayout()
        ln_layout.addWidget(ln_lab)
        ln_layout.addWidget(self.ln_tbox)

        # first name box
        fn_lab = QLabel('First Name column')
        self.fn_tbox = QLineEdit()
        self.fn_tbox.setText(a.yba_firstcol)
        self.fn_tbox.textChanged.connect(self.fn_tbox_var)

        fn_layout = QVBoxLayout()
        fn_layout.addWidget(fn_lab)
        fn_layout.addWidget(self.fn_tbox)

        glayout = QVBoxLayout()
        glayout.addLayout(ln_layout)
        glayout.addLayout(fn_layout)
        
        # dropdown
        divider_label = QLabel('Class Divider')
        self.divider_type = QComboBox()
        self.divider_type.addItem('Sheet')
        self.divider_type.addItem('Column')
        self.divider_type.currentIndexChanged.connect(self.dropdown_changed)
        self.divider_var = QLineEdit()
        self.divider_var.setFixedWidth(65)
        self.divider_var.textChanged.connect(self.var_changed)
        self.divider_var.setPlaceholderText('Column')
        self.divider_var_check = QLineEdit()
        self.divider_var_check.setFixedWidth(45)
        self.divider_var_check.textChanged.connect(self.var_check_changed)
        self.divider_var_check.setPlaceholderText('Val')
        self.divider_var.setText(a.yba_gradesep)
        self.divider_var_check.setText(a.yba_gradesepv)
        if a.yba_gradecos == 'Sheet':
            self.divider_type.setCurrentIndex(0)
            self.divider_var.hide()
            self.divider_var_check.hide()
        elif a.yba_gradecos == 'Column':
            self.divider_type.setCurrentIndex(1)

        div_sublayout = QHBoxLayout()
        div_sublayout.addWidget(self.divider_type)
        div_sublayout.addWidget(self.divider_var)
        div_sublayout.addWidget(self.divider_var_check)

        div_layout = QVBoxLayout()
        div_layout.addWidget(divider_label)
        div_layout.addLayout(div_sublayout)
        glayout.addLayout(div_layout)
        
        groupbox.setLayout(glayout)

        mlayout = QVBoxLayout(self)
        mlayout.addWidget(groupbox)
        self.setLayout(mlayout)

    def ln_tbox_var(self, data):
        a.yba_lastcol = data
        p(data)

    def fn_tbox_var(self, data):
        a.yba_firstcol = data
        p(data)
    
    def dropdown_changed(self, data):
        p(f'Dropdown Changed! {data}, {self.divider_type.currentText()}')
        a.yba_gradecos = self.divider_type.currentText()
        if data == 0: 
            self.divider_var.hide()
            self.divider_var_check.hide()
        else:
            self.divider_var.show()
            self.divider_var_check.show()

    def var_changed(self, data):
        p(f'Var changed, {data}')
        a.yba_gradesep = data

    def var_check_changed(self, data):
        p(f'Var_check changed, {data}')
        a.yba_gradesepv = data

    def configchange(self):
        self.ln_tbox.setText(a.yba_lastcol)
        self.fn_tbox.setText(a.yba_firstcol)
        self.divider_var.setText(a.yba_gradesep)
        self.divider_var_check.setText(a.yba_gradesepv)
        if a.yba_gradecos == 'Sheet':
            self.divider_type.setCurrentIndex(0)
            self.divider_var.hide()
            self.divider_var_check.hide()
        elif a.yba_gradecos == 'Column':
            self.divider_type.setCurrentIndex(1)

