# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_v01.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1190, 732)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"color: rgb(210, 210, 210);")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_title = QLabel(self.widget)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout_9.addWidget(self.label_title, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_9 = QFrame(self.widget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../PythonEnv/GUI/Simple_PySide_Base-master/icons/24x24/cil-settings.png"))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_version = QLabel(self.frame_8)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.verticalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.top_frame2 = QFrame(self.widget)
        self.top_frame2.setObjectName(u"top_frame2")
        self.top_frame2.setMinimumSize(QSize(0, 50))
        self.top_frame2.setFrameShape(QFrame.StyledPanel)
        self.top_frame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.top_frame2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_7 = QLineEdit(self.top_frame2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	font: 10pt;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_10.addWidget(self.lineEdit_7)

        self.pushButton = QPushButton(self.top_frame2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 30))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255,255,255);\n"
"font: 10pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../PythonEnv/GUI/Simple_PySide_Base-master/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.top_frame2)

        self.middle_frame = QFrame(self.widget)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.middle_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_panel = QFrame(self.middle_frame)
        self.left_panel.setObjectName(u"left_panel")
        self.left_panel.setMinimumSize(QSize(0, 300))
        self.left_panel.setFrameShape(QFrame.StyledPanel)
        self.left_panel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_panel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_panel)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	font: 10pt;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QToolTip {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0); \n"
"	border: black solid 1px\n"
" };\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	font: 10pt;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_panel)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QToolTip {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0); \n"
"	border: black solid 1px\n"
" };\n"
"\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	font: 10pt;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_7.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.left_panel)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QToolTip {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0); \n"
"	border: black solid 1px\n"
" };\n"
"\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	font: 10pt;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.left_panel)

        self.middle_panel = QFrame(self.middle_frame)
        self.middle_panel.setObjectName(u"middle_panel")
        self.middle_panel.setStyleSheet(u"background-color: rgba(27, 29, 35, 160);\n"
"")
        self.middle_panel.setFrameShape(QFrame.StyledPanel)
        self.middle_panel.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.middle_panel)

        self.right_panel = QFrame(self.middle_frame)
        self.right_panel.setObjectName(u"right_panel")
        self.right_panel.setFrameShape(QFrame.StyledPanel)
        self.right_panel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_panel)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.right_panel)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QToolTip {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0); \n"
"	border: black solid 1px\n"
" };\n"
"\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	font: 10pt;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.right_panel)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QToolTip {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0); \n"
"	border: black solid 1px\n"
" };\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	font: 10pt;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_5.addWidget(self.lineEdit_4)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.right_panel)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"/*color: rgb(255, 255, 255);*/\n"
"font: 75 10pt;")

        self.horizontalLayout_8.addWidget(self.label_7)

        #self.checkBox = QCheckBox(self.frame_6)
        #self.checkBox.setObjectName(u"checkBox")
        #self.checkBox.setStyleSheet(u"")

        #self.horizontalLayout_8.addWidget(self.checkBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.right_panel)


        self.verticalLayout_5.addWidget(self.middle_frame)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.button_run = QPushButton(self.frame_7)
        self.button_run.setObjectName(u"button_run")
        self.button_run.setMinimumSize(QSize(200, 40))
        self.button_run.setMaximumSize(QSize(16777215, 16777215))
        self.button_run.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255,255,255);\n"
"	font: 15pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.verticalLayout_6.addWidget(self.button_run, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.bottom_frame = QFrame(self.widget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bottom_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.bottom_frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 300))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.progressBar = QProgressBar(self.bottom_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.progressBar.setValue(23)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_5.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">Fundamentus Data</span></p></body></html>", None))
        self.label.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">V 1.0</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Limite Inferior (bilhoes)", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Microcaps: valor &lt; 3 bi</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Smallcaps: 3 bi &lt; valor &lt; 5 bi</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Midcaps: 5 bi &lt; valor &lt; 10 bi</span></p>\n"
"<p style=\" margin-t"
                        "op:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Largecaps: valor &gt; 10bi</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">&lt; Valor de Mercado &lt;</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Limite Superior (bilhoes)", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Padrao: &gt; 5</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">R.O.E. &gt;</span></p></body></html>", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Limite Inferior", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Padrao: &gt; 1.5</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">L.C. &gt;</span></p></body></html>", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Limite Inferior", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Padrao: &lt; 0.5</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Div / Pat &lt;</span></p></body></html>", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Limite Superior", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Padrao: &lt; 3</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Div / EBITDA &lt;</span></p></body></html>", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Limite Superior", None))
        #self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Separar tabelas por setor?</span></p></body></html>", None))
        #self.checkBox.setText("")
        self.button_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
    # retranslateUi

