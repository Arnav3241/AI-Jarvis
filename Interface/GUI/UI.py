# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##-+
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
        MainWindow.resize(1980, 1091)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"\n"
"background-color: rgb(0, 0, 0);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textDisplayConversation = QTextBrowser(self.centralwidget)
        self.textDisplayConversation.setObjectName(u"textDisplayConversation")
        self.textDisplayConversation.setGeometry(QRect(1410, 290, 471, 541))
        font = QFont()
        font.setPointSize(10)
        self.textDisplayConversation.setFont(font)
        self.textDisplayConversation.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:1px solid;\n"
"border-color: rgb(85, 170, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 15, 108, 255))")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1410, 270, 471, 21))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(670, 10, 1241, 201))
        self.label.setStyleSheet(u"font: 100pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-20, 740, 981, 451))
        self.label_3.setPixmap(QPixmap(u"C:/Users/hp/Downloads/AI-Project-JARVIS-main/AI-Project-JARVIS-main/gif/51.gif"))
        self.label_3.setScaledContents(True)
        self.display = QLabel(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(1190, 870, 901, 121))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(50)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.display.setFont(font1)
        self.display.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:0px solid;\n"
"font:50pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 210, 981, 691))
        self.label_4.setPixmap(QPixmap(u"C:/Users/hp/Downloads/VoiceReg/Ntuks.gif"))
        self.label_4.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 870, 1981, 5))
        self.label_2.setStyleSheet(u"background-color:rgb(0, 0, 255)")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 40, 441, 371))
        self.label_5.setPixmap(QPixmap(u"C:/Users/hp/Downloads/B.G/gyhf.jpg"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 420, 441, 371))
        self.label_6.setPixmap(QPixmap(u"C:/Users/hp/Downloads/B.G/gyhf.jpg"))
        self.label_6.setScaledContents(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 210, 451, 31))
        self.label_8.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 590, 451, 31))
        self.label_10.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.str_btn = QLabel(self.centralwidget)
        self.str_btn.setObjectName(u"str_btn")
        self.str_btn.setGeometry(QRect(1420, 20, 441, 131))
        self.str_btn.setPixmap(QPixmap(u"C:/Users/hp/Downloads/Buttons/Start.png"))
        self.str_btn.setScaledContents(True)
        self.end_btn = QLabel(self.centralwidget)
        self.end_btn.setObjectName(u"end_btn")
        self.end_btn.setGeometry(QRect(1420, 140, 441, 131))
        self.end_btn.setPixmap(QPixmap(u"C:/Users/hp/Downloads/Buttons/Quit.png"))
        self.end_btn.setScaledContents(True)
        self.yt_btn = QLabel(self.centralwidget)
        self.yt_btn.setObjectName(u"yt_btn")
        self.yt_btn.setGeometry(QRect(120, 70, 231, 121))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(35)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.yt_btn.setFont(font2)
        self.yt_btn.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:0px solid;\n"
"font:35pt \"MS Shell Dlg 2\";")
        self.google = QLabel(self.centralwidget)
        self.google.setObjectName(u"google")
        self.google.setGeometry(QRect(130, 260, 231, 121))
        self.google.setFont(font2)
        self.google.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:0px solid;\n"
"font:35pt \"MS Shell Dlg 2\";")
        self.google_2 = QLabel(self.centralwidget)
        self.google_2.setObjectName(u"google_2")
        self.google_2.setGeometry(QRect(100, 460, 271, 121))
        self.google_2.setFont(font2)
        self.google_2.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:0px solid;\n"
"font:35pt \"MS Shell Dlg 2\";")
        self.google_3 = QLabel(self.centralwidget)
        self.google_3.setObjectName(u"google_3")
        self.google_3.setGeometry(QRect(100, 640, 271, 121))
        self.google_3.setFont(font2)
        self.google_3.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:0px solid;\n"
"font:35pt \"MS Shell Dlg 2\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  Response Box", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Jarvis", None))
        self.label_3.setText("")
        self.display.setText(QCoreApplication.translate("MainWindow", u"Recognizing...", None))
        self.label_4.setText("")
        self.label_2.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_10.setText("")
        self.str_btn.setText("")
        self.end_btn.setText("")
        self.yt_btn.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.google.setText(QCoreApplication.translate("MainWindow", u"Google", None))
        self.google_2.setText(QCoreApplication.translate("MainWindow", u"Whatsapp", None))
        self.google_3.setText(QCoreApplication.translate("MainWindow", u"G-mail", None))
    # retranslateUi

