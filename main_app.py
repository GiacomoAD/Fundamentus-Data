# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:12:14 2021

@author: GiacomoAD
"""


import sys
import os
import platform
from fundamentus_GUI import Ui_MainWindow
from app_functions import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle('Fundamentus Data v1.0.0')

        
        
        
        self.ui.lineEdit_7.setReadOnly(True)
        
        diretorio = os.getcwd() 

        diretorio = diretorio + r'\PlanilhaSaida.xlsx'
        
        self.ui.lineEdit_7.setText(diretorio)
        
      
        
        self.signal = MySignal()
        self.signal.sig_with_str.connect(self.print_console_log)
        self.signal.sig_with_int.connect(self.change_progress_bar)
        self.ui.progressBar.setValue(0)
        
        self.ui.pushButton.clicked.connect(lambda: appFunctions.chooseFile(self))
        self.ui.button_run.clicked.connect(lambda: appFunctions.runApp(self, self.signal.sig_with_str, self.signal.sig_with_int))
        
        
    def print_console_log(self, str):
        self.ui.plainTextEdit.setPlainText( self.ui.plainTextEdit.toPlainText() + str)
        
    def change_progress_bar(self, value, maxValue):
        self.ui.progressBar.setMaximum(maxValue)
        self.ui.progressBar.setValue(value)
        
        if(value == maxValue):
            self.ui.button_run.setEnabled(True)
            self.ui.lineEdit.setReadOnly(False)
            self.ui.lineEdit_2.setReadOnly(False)
            self.ui.lineEdit_5.setReadOnly(False)
            self.ui.lineEdit_6.setReadOnly(False)
            self.ui.lineEdit_3.setReadOnly(False)
            self.ui.lineEdit_4.setReadOnly(False)
        
class MySignal(QtCore.QObject):
    sig_with_str = QtCore.Signal(str)
    sig_with_int = QtCore.Signal(int, int)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())