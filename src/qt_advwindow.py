from PySide6.QtWidgets import (QDialog, QLineEdit, QPushButton, QHBoxLayout,
                                QGroupBox, QVBoxLayout, QComboBox, QLabel)
import qt_adv_vars as a
from debugprint import p
def echo(data):
    print('qt_advwindow present')
class advwindow(QDialog):
    def __init__(self):
        super().__init__()
        
        # last name box
        ln_lab = QLabel('Last Name column')
        ln_tbox = QLineEdit()
        ln_tbox.textChanged.connect(self.ln_tbox_var)

        ln_layout = QVBoxLayout()
        ln_layout.addWidget(ln_lab)
        ln_layout.addWidget(ln_tbox)

        # first name box
        fn_lab = QLabel('First Name column')
        fn_tbox = QLineEdit()
        fn_tbox.textChanged.connect(self.fn_tbox_var)

        fn_layout = QVBoxLayout()
        fn_layout.addWidget(fn_lab)
        fn_layout.addWidget(fn_tbox)

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

        div_sublayout = QHBoxLayout()
        div_sublayout.addWidget(self.divider_type)
        div_sublayout.addWidget(self.divider_var)

        div_layout = QVBoxLayout()
        div_layout.addWidget(divider_label)
        div_layout.addLayout(div_sublayout)
        glayout.addLayout(div_layout)
    
        if a.pg_or_yba == 'pg':
            groupbox = QGroupBox('Roster Advanced Window')
            ln_tbox.setText(a.pg_lastcol)
            fn_tbox.setText(a.pg_firstcol)

            if a.pg_gradecos == 'Sheet':
                self.divider_type.setCurrentIndex(0)
                self.divider_var.hide()
            elif a.pg_gradecos == 'Column':
                self.divider_type.setCurrentIndex(1)
            self.divider_var.setText(a.pg_gradesep)
            
        elif a.pg_or_yba == 'yba':
            groupbox = QGroupBox('Covrep Advanced Window')
            ln_tbox.setText(a.yba_lastcol)
            fn_tbox.setText(a.yba_firstcol)

            if a.yba_gradecos == 'Sheet':
                self.divider_type.setCurrentIndex(0)
                self.divider_var.hide()
            elif a.yba_gradecos == 'Column':
                self.divider_type.setCurrentIndex(1)
            self.divider_var.setText(a.yba_gradesep)


        else:
            raise ValueError('Improper value for q.pg_or_yba')
        

        groupbox.setLayout(glayout)

        mlayout = QVBoxLayout(self)
        mlayout.addWidget(groupbox)
        self.setLayout(mlayout)

    def ln_tbox_var(self, data):
        if a.pg_or_yba == 'pg':
            a.pg_lastcol = data
            p(data)
        elif a.pg_or_yba == 'yba':
            a.yba_lastcol = data
            p(data)

    def fn_tbox_var(self, data):
        if a.pg_or_yba == 'pg':
            a.pg_firstcol = data
            p(data)
        elif a.pg_or_yba == 'yba':
            a.yba_firstcol = data
            p(data)
    
    def dropdown_changed(self, data):
        p(f'Dropdown Changed! {data}, {self.divider_type.currentText()}')
        if a.pg_or_yba == 'pg':
            a.pg_gradecos = self.divider_type.currentText()
        elif a.pg_or_yba == 'yba':
            a.yba_gradecos = self.divider_type.currentText()
        if data == 0: 
            self.divider_var.hide()
        else:
            self.divider_var.show()

    def var_changed(self, data):
        p(f'Var changed, {data}')
        if a.pg_or_yba == 'pg':
            a.pg_gradesep = data
        elif a.pg_or_yba == 'yba':
            a.yba_gradesep = data

