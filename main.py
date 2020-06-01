# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cryto.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ImplementProccess as proccess
import time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QMainWindow {\n"
"    background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"    color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"    color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(230, 230, 230);\n"
"    border-style: solid;\n"
"    background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"    color: #000000;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #000000;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    color: #000000;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(223,223,223);\n"
"        background-color:rgb(226,226,226);\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"      border-bottom-width:1px;\n"
"      border-top-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #000000;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"}\n"
"QRadioButton {\n"
"    color: 000000;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_encrypt = QtWidgets.QWidget()
        self.tab_encrypt.setEnabled(True)
        self.tab_encrypt.setObjectName("tab_encrypt")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_encrypt)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEditEnSource = QtWidgets.QLineEdit(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.lineEditEnSource.sizePolicy().hasHeightForWidth())
        self.lineEditEnSource.setSizePolicy(sizePolicy)
        self.lineEditEnSource.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditEnSource.setSizeIncrement(QtCore.QSize(0, 50))
        self.lineEditEnSource.setBaseSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditEnSource.setFont(font)
        self.lineEditEnSource.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditEnSource.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditEnSource.setClearButtonEnabled(False)
        self.lineEditEnSource.setObjectName("lineEditEnSource")
        self.gridLayout_4.addWidget(self.lineEditEnSource, 2, 5, 1, 2)
        self.lineEditEnOut = QtWidgets.QLineEdit(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.lineEditEnOut.sizePolicy().hasHeightForWidth())
        self.lineEditEnOut.setSizePolicy(sizePolicy)
        self.lineEditEnOut.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditEnOut.setSizeIncrement(QtCore.QSize(0, 50))
        self.lineEditEnOut.setBaseSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditEnOut.setFont(font)
        self.lineEditEnOut.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditEnOut.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditEnOut.setClearButtonEnabled(False)
        self.lineEditEnOut.setObjectName("lineEditEnOut")
        self.gridLayout_4.addWidget(self.lineEditEnOut, 6, 5, 1, 2)
        self.pushButtonEnFolder = QtWidgets.QPushButton(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEnFolder.sizePolicy().hasHeightForWidth())
        self.pushButtonEnFolder.setSizePolicy(sizePolicy)
        self.pushButtonEnFolder.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonEnFolder.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEnFolder.setIcon(icon1)
        self.pushButtonEnFolder.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonEnFolder.setAutoDefault(False)
        self.pushButtonEnFolder.setDefault(True)
        self.pushButtonEnFolder.setObjectName("pushButtonEnFolder")
        self.gridLayout_4.addWidget(self.pushButtonEnFolder, 3, 7, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 5, 5, 1, 2)
        self.pushButtonEnCreate = QtWidgets.QPushButton(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEnCreate.sizePolicy().hasHeightForWidth())
        self.pushButtonEnCreate.setSizePolicy(sizePolicy)
        self.pushButtonEnCreate.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonEnCreate.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/generator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEnCreate.setIcon(icon2)
        self.pushButtonEnCreate.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonEnCreate.setDefault(True)
        self.pushButtonEnCreate.setObjectName("pushButtonEnCreate")
        self.gridLayout_4.addWidget(self.pushButtonEnCreate, 5, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setLineWidth(2)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 3, 5, 1, 2)
        self.radioEnAES = QtWidgets.QRadioButton(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioEnAES.setFont(font)
        self.radioEnAES.setObjectName("radioEnAES")
        self.gridLayout_4.addWidget(self.radioEnAES, 0, 5, 1, 1)
        self.checkBoxEnSource = QtWidgets.QCheckBox(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxEnSource.setFont(font)
        self.checkBoxEnSource.setIconSize(QtCore.QSize(25, 25))
        self.checkBoxEnSource.setTristate(False)
        self.checkBoxEnSource.setObjectName("checkBoxEnSource")
        self.gridLayout_4.addWidget(self.checkBoxEnSource, 7, 5, 1, 1)
        self.pushButtonEnKey = QtWidgets.QPushButton(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEnKey.sizePolicy().hasHeightForWidth())
        self.pushButtonEnKey.setSizePolicy(sizePolicy)
        self.pushButtonEnKey.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonEnKey.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEnKey.setIcon(icon3)
        self.pushButtonEnKey.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonEnKey.setDefault(True)
        self.pushButtonEnKey.setObjectName("pushButtonEnKey")
        self.gridLayout_4.addWidget(self.pushButtonEnKey, 4, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 4, 1, 1)
        self.radioEn3DES = QtWidgets.QRadioButton(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioEn3DES.setFont(font)
        self.radioEn3DES.setObjectName("radioEn3DES")
        self.gridLayout_4.addWidget(self.radioEn3DES, 0, 7, 1, 1)
        self.radioEnRSA = QtWidgets.QRadioButton(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioEnRSA.setFont(font)
        self.radioEnRSA.setObjectName("radioEnRSA")
        self.gridLayout_4.addWidget(self.radioEnRSA, 0, 6, 1, 1)
        self.lineEditEnKey = QtWidgets.QLineEdit(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.lineEditEnKey.sizePolicy().hasHeightForWidth())
        self.lineEditEnKey.setSizePolicy(sizePolicy)
        self.lineEditEnKey.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditEnKey.setSizeIncrement(QtCore.QSize(0, 50))
        self.lineEditEnKey.setBaseSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditEnKey.setFont(font)
        self.lineEditEnKey.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditEnKey.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditEnKey.setClearButtonEnabled(False)
        self.lineEditEnKey.setObjectName("lineEditEnKey")
        self.gridLayout_4.addWidget(self.lineEditEnKey, 4, 5, 1, 2)
        self.label = QtWidgets.QLabel(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_encrypt)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 1, 4, 1, 4)
        self.progressBarEn = QtWidgets.QProgressBar(self.tab_encrypt)
        self.progressBarEn.setProperty("value", 0)
        self.progressBarEn.setObjectName("progressBarEn")
        self.gridLayout_4.addWidget(self.progressBarEn, 12, 4, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 6, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 11, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 4, 4, 1, 1)
        self.pushButtonEnOut = QtWidgets.QPushButton(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEnOut.sizePolicy().hasHeightForWidth())
        self.pushButtonEnOut.setSizePolicy(sizePolicy)
        self.pushButtonEnOut.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonEnOut.setFont(font)
        self.pushButtonEnOut.setIcon(icon1)
        self.pushButtonEnOut.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonEnOut.setDefault(True)
        self.pushButtonEnOut.setObjectName("pushButtonEnOut")
        self.gridLayout_4.addWidget(self.pushButtonEnOut, 6, 7, 1, 1)
        self.pushButtonEnFile = QtWidgets.QPushButton(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEnFile.sizePolicy().hasHeightForWidth())
        self.pushButtonEnFile.setSizePolicy(sizePolicy)
        self.pushButtonEnFile.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonEnFile.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/Open.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEnFile.setIcon(icon4)
        self.pushButtonEnFile.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonEnFile.setAutoDefault(False)
        self.pushButtonEnFile.setDefault(True)
        self.pushButtonEnFile.setObjectName("pushButtonEnFile")
        self.gridLayout_4.addWidget(self.pushButtonEnFile, 2, 7, 1, 1)
        self.pushButtonEnStart = QtWidgets.QPushButton(self.tab_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEnStart.sizePolicy().hasHeightForWidth())
        self.pushButtonEnStart.setSizePolicy(sizePolicy)
        self.pushButtonEnStart.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEnStart.setFont(font)
        self.pushButtonEnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/encrypt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEnStart.setIcon(icon5)
        self.pushButtonEnStart.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonEnStart.setDefault(True)
        self.pushButtonEnStart.setObjectName("pushButtonEnStart")
        self.gridLayout_4.addWidget(self.pushButtonEnStart, 8, 7, 2, 1)
        self.checkBoxEnDelete = QtWidgets.QCheckBox(self.tab_encrypt)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxEnDelete.setFont(font)
        self.checkBoxEnDelete.setObjectName("checkBoxEnDelete")
        self.gridLayout_4.addWidget(self.checkBoxEnDelete, 8, 5, 1, 1)
        self.tabWidget.addTab(self.tab_encrypt, icon5, "")
        self.tab_decrypt = QtWidgets.QWidget()
        self.tab_decrypt.setObjectName("tab_decrypt")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_decrypt)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.pushButtonDeFolder = QtWidgets.QPushButton(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeFolder.sizePolicy().hasHeightForWidth())
        self.pushButtonDeFolder.setSizePolicy(sizePolicy)
        self.pushButtonDeFolder.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonDeFolder.setFont(font)
        self.pushButtonDeFolder.setIcon(icon1)
        self.pushButtonDeFolder.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonDeFolder.setDefault(True)
        self.pushButtonDeFolder.setObjectName("pushButtonDeFolder")
        self.gridLayout.addWidget(self.pushButtonDeFolder, 3, 3, 1, 1)
        self.pushButtonDeFile = QtWidgets.QPushButton(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeFile.sizePolicy().hasHeightForWidth())
        self.pushButtonDeFile.setSizePolicy(sizePolicy)
        self.pushButtonDeFile.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonDeFile.setFont(font)
        self.pushButtonDeFile.setIcon(icon4)
        self.pushButtonDeFile.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonDeFile.setDefault(True)
        self.pushButtonDeFile.setObjectName("pushButtonDeFile")
        self.gridLayout.addWidget(self.pushButtonDeFile, 2, 3, 1, 1)
        self.pushButtonDeKey = QtWidgets.QPushButton(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeKey.sizePolicy().hasHeightForWidth())
        self.pushButtonDeKey.setSizePolicy(sizePolicy)
        self.pushButtonDeKey.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonDeKey.setFont(font)
        self.pushButtonDeKey.setIcon(icon3)
        self.pushButtonDeKey.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonDeKey.setDefault(True)
        self.pushButtonDeKey.setObjectName("pushButtonDeKey")
        self.gridLayout.addWidget(self.pushButtonDeKey, 4, 3, 1, 1)
        self.pushButtonDeOut = QtWidgets.QPushButton(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeOut.sizePolicy().hasHeightForWidth())
        self.pushButtonDeOut.setSizePolicy(sizePolicy)
        self.pushButtonDeOut.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonDeOut.setFont(font)
        self.pushButtonDeOut.setIcon(icon1)
        self.pushButtonDeOut.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonDeOut.setDefault(True)
        self.pushButtonDeOut.setObjectName("pushButtonDeOut")
        self.gridLayout.addWidget(self.pushButtonDeOut, 6, 3, 1, 1)
        self.pushButtonDeStart = QtWidgets.QPushButton(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeStart.sizePolicy().hasHeightForWidth())
        self.pushButtonDeStart.setSizePolicy(sizePolicy)
        self.pushButtonDeStart.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDeStart.setFont(font)
        self.pushButtonDeStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/decrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDeStart.setIcon(icon6)
        self.pushButtonDeStart.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonDeStart.setDefault(True)
        self.pushButtonDeStart.setObjectName("pushButtonDeStart")
        self.gridLayout.addWidget(self.pushButtonDeStart, 8, 3, 1, 1)
        self.radioButtonDeAES = QtWidgets.QRadioButton(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonDeAES.setFont(font)
        self.radioButtonDeAES.setObjectName("radioButtonDeAES")
        self.gridLayout.addWidget(self.radioButtonDeAES, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_decrypt)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.radioButtonDe3DES = QtWidgets.QRadioButton(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonDe3DES.setFont(font)
        self.radioButtonDe3DES.setObjectName("radioButtonDe3DES")
        self.gridLayout.addWidget(self.radioButtonDe3DES, 0, 3, 1, 1)
        self.lineEditDeKey = QtWidgets.QLineEdit(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.lineEditDeKey.sizePolicy().hasHeightForWidth())
        self.lineEditDeKey.setSizePolicy(sizePolicy)
        self.lineEditDeKey.setMinimumSize(QtCore.QSize(611, 30))
        self.lineEditDeKey.setSizeIncrement(QtCore.QSize(0, 50))
        self.lineEditDeKey.setBaseSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDeKey.setFont(font)
        self.lineEditDeKey.setObjectName("lineEditDeKey")
        self.gridLayout.addWidget(self.lineEditDeKey, 4, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEditDeOut = QtWidgets.QLineEdit(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.lineEditDeOut.sizePolicy().hasHeightForWidth())
        self.lineEditDeOut.setSizePolicy(sizePolicy)
        self.lineEditDeOut.setMinimumSize(QtCore.QSize(611, 30))
        self.lineEditDeOut.setSizeIncrement(QtCore.QSize(0, 50))
        self.lineEditDeOut.setBaseSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDeOut.setFont(font)
        self.lineEditDeOut.setObjectName("lineEditDeOut")
        self.gridLayout.addWidget(self.lineEditDeOut, 6, 1, 1, 2)
        self.radioButtonDeRSA = QtWidgets.QRadioButton(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonDeRSA.setFont(font)
        self.radioButtonDeRSA.setObjectName("radioButtonDeRSA")
        self.gridLayout.addWidget(self.radioButtonDeRSA, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setLineWidth(2)
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 1, 1, 2)
        self.progressBarDe = QtWidgets.QProgressBar(self.tab_decrypt)
        self.progressBarDe.setProperty("value", 0)
        self.progressBarDe.setObjectName("progressBarDe")
        self.gridLayout.addWidget(self.progressBarDe, 10, 0, 1, 4)
        self.lineEditDeSource = QtWidgets.QLineEdit(self.tab_decrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.lineEditDeSource.sizePolicy().hasHeightForWidth())
        self.lineEditDeSource.setSizePolicy(sizePolicy)
        self.lineEditDeSource.setMinimumSize(QtCore.QSize(611, 30))
        self.lineEditDeSource.setSizeIncrement(QtCore.QSize(0, 50))
        self.lineEditDeSource.setBaseSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDeSource.setFont(font)
        self.lineEditDeSource.setObjectName("lineEditDeSource")
        self.gridLayout.addWidget(self.lineEditDeSource, 2, 1, 1, 2)
        self.checkBoxDeSource = QtWidgets.QCheckBox(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxDeSource.setFont(font)
        self.checkBoxDeSource.setObjectName("checkBoxDeSource")
        self.gridLayout.addWidget(self.checkBoxDeSource, 7, 1, 1, 1)
        self.checkBoxDeDelete = QtWidgets.QCheckBox(self.tab_decrypt)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxDeDelete.setFont(font)
        self.checkBoxDeDelete.setObjectName("checkBoxDeDelete")
        self.gridLayout.addWidget(self.checkBoxDeDelete, 8, 1, 1, 1)
        self.tabWidget.addTab(self.tab_decrypt, icon6, "")
        self.tab_generator = QtWidgets.QWidget()
        self.tab_generator.setObjectName("tab_generator")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_generator)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_generator)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabSym = QtWidgets.QWidget()
        self.tabSym.setObjectName("tabSym")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabSym)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_18 = QtWidgets.QLabel(self.tabSym)
        self.label_18.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tabSym)
        self.label_19.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 0, 0, 1, 1)
        self.lineEditSymLength = QtWidgets.QLineEdit(self.tabSym)
        self.lineEditSymLength.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEditSymLength.setObjectName("lineEditSymLength")
        self.gridLayout_5.addWidget(self.lineEditSymLength, 1, 1, 1, 2)
        self.pushButtonSymCopy = QtWidgets.QPushButton(self.tabSym)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSymCopy.sizePolicy().hasHeightForWidth())
        self.pushButtonSymCopy.setSizePolicy(sizePolicy)
        self.pushButtonSymCopy.setMinimumSize(QtCore.QSize(180, 0))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSymCopy.setIcon(icon7)
        self.pushButtonSymCopy.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonSymCopy.setDefault(True)
        self.pushButtonSymCopy.setObjectName("pushButtonSymCopy")
        self.gridLayout_5.addWidget(self.pushButtonSymCopy, 0, 4, 1, 1)
        self.pushButtonSymGenerate = QtWidgets.QPushButton(self.tabSym)
        self.pushButtonSymGenerate.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSymGenerate.setFont(font)
        self.pushButtonSymGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSymGenerate.setIcon(icon2)
        self.pushButtonSymGenerate.setIconSize(QtCore.QSize(80, 80))
        self.pushButtonSymGenerate.setAutoDefault(False)
        self.pushButtonSymGenerate.setDefault(True)
        self.pushButtonSymGenerate.setObjectName("pushButtonSymGenerate")
        self.gridLayout_5.addWidget(self.pushButtonSymGenerate, 2, 2, 1, 1)
        self.pushButtonSymSave = QtWidgets.QPushButton(self.tabSym)
        self.pushButtonSymSave.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSymSave.setFont(font)
        self.pushButtonSymSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/save.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSymSave.setIcon(icon8)
        self.pushButtonSymSave.setIconSize(QtCore.QSize(80, 80))
        self.pushButtonSymSave.setDefault(True)
        self.pushButtonSymSave.setObjectName("pushButtonSymSave")
        self.gridLayout_5.addWidget(self.pushButtonSymSave, 2, 3, 1, 1)
        self.lineEditSymKey = QtWidgets.QLineEdit(self.tabSym)
        self.lineEditSymKey.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEditSymKey.setReadOnly(True)
        self.lineEditSymKey.setObjectName("lineEditSymKey")
        self.gridLayout_5.addWidget(self.lineEditSymKey, 0, 1, 1, 3)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/Symmetric.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tabSym, icon9, "")
        self.tabAsym = QtWidgets.QWidget()
        self.tabAsym.setObjectName("tabAsym")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabAsym)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 3, 1, 1)
        self.comboBoxAsym = QtWidgets.QComboBox(self.tabAsym)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxAsym.sizePolicy().hasHeightForWidth())
        self.comboBoxAsym.setSizePolicy(sizePolicy)
        self.comboBoxAsym.setMinimumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxAsym.setFont(font)
        self.comboBoxAsym.setEditable(False)
        self.comboBoxAsym.setCurrentText("")
        self.comboBoxAsym.setMaxVisibleItems(4)
        self.comboBoxAsym.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBoxAsym.setObjectName("comboBoxAsym")
        self.gridLayout_6.addWidget(self.comboBoxAsym, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tabAsym)
        self.label_20.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 0, 1, 1)
        self.pushButtonAsymGenerate = QtWidgets.QPushButton(self.tabAsym)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAsymGenerate.sizePolicy().hasHeightForWidth())
        self.pushButtonAsymGenerate.setSizePolicy(sizePolicy)
        self.pushButtonAsymGenerate.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAsymGenerate.setFont(font)
        self.pushButtonAsymGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAsymGenerate.setIcon(icon2)
        self.pushButtonAsymGenerate.setIconSize(QtCore.QSize(80, 80))
        self.pushButtonAsymGenerate.setDefault(True)
        self.pushButtonAsymGenerate.setObjectName("pushButtonAsymGenerate")
        self.gridLayout_6.addWidget(self.pushButtonAsymGenerate, 1, 1, 1, 2)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/Asymmetric.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tabAsym, icon10, "")
        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_generator, icon2, "")
        self.tab_hash = QtWidgets.QWidget()
        self.tab_hash.setObjectName("tab_hash")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_hash)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_16 = QtWidgets.QLabel(self.tab_hash)
        self.label_16.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.lineEditHash2 = QtWidgets.QLineEdit(self.tab_hash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHash2.sizePolicy().hasHeightForWidth())
        self.lineEditHash2.setSizePolicy(sizePolicy)
        self.lineEditHash2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEditHash2.setObjectName("lineEditHash2")
        self.gridLayout_2.addWidget(self.lineEditHash2, 3, 1, 1, 2)
        self.lineEditHash1 = QtWidgets.QLineEdit(self.tab_hash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHash1.sizePolicy().hasHeightForWidth())
        self.lineEditHash1.setSizePolicy(sizePolicy)
        self.lineEditHash1.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEditHash1.setObjectName("lineEditHash1")
        # set font size hash
        f = self.lineEditHash1.font()
        f.setPointSize(12) # sets the size to 12
        self.lineEditHash1.setFont(f)

        f = self.lineEditHash2.font()
        f.setPointSize(12) # sets the size to 12
        self.lineEditHash2.setFont(f)
        # set font size
        self.gridLayout_2.addWidget(self.lineEditHash1, 2, 1, 1, 2)
        self.pushButtonHashVerify = QtWidgets.QPushButton(self.tab_hash)
        self.pushButtonHashVerify.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonHashVerify.setFont(font)
        self.pushButtonHashVerify.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/verify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonHashVerify.setIcon(icon11)
        self.pushButtonHashVerify.setIconSize(QtCore.QSize(50, 50))
        self.pushButtonHashVerify.setDefault(True)
        self.pushButtonHashVerify.setObjectName("pushButtonHashVerify")
        self.gridLayout_2.addWidget(self.pushButtonHashVerify, 4, 2, 1, 1)
        self.pushButtonHashFile2 = QtWidgets.QPushButton(self.tab_hash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonHashFile2.sizePolicy().hasHeightForWidth())
        self.pushButtonHashFile2.setSizePolicy(sizePolicy)
        self.pushButtonHashFile2.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonHashFile2.setFont(font)
        self.pushButtonHashFile2.setAutoFillBackground(False)
        self.pushButtonHashFile2.setIcon(icon4)
        self.pushButtonHashFile2.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonHashFile2.setDefault(True)
        self.pushButtonHashFile2.setObjectName("pushButtonHashFile2")
        self.gridLayout_2.addWidget(self.pushButtonHashFile2, 3, 3, 1, 1)
        self.pushButtonHashFile1 = QtWidgets.QPushButton(self.tab_hash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonHashFile1.sizePolicy().hasHeightForWidth())
        self.pushButtonHashFile1.setSizePolicy(sizePolicy)
        self.pushButtonHashFile1.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonHashFile1.setFont(font)
        self.pushButtonHashFile1.setAutoFillBackground(False)
        self.pushButtonHashFile1.setIcon(icon4)
        self.pushButtonHashFile1.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonHashFile1.setDefault(True)
        self.pushButtonHashFile1.setObjectName("pushButtonHashFile1")
        self.gridLayout_2.addWidget(self.pushButtonHashFile1, 2, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab_hash)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 4)
        self.label_17 = QtWidgets.QLabel(self.tab_hash)
        self.label_17.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_hash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/hash.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_hash, icon12, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1237, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setIcon(icon4)
        self.actionOpen_File.setShortcutVisibleInContextMenu(False)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setIcon(icon1)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/quit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap("icon/quit.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon13)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRead_me = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon/readme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRead_me.setIcon(icon14)
        self.actionRead_me.setObjectName("actionRead_me")
        self.actionImport_Key = QtWidgets.QAction(MainWindow)
        self.actionImport_Key.setIcon(icon3)
        self.actionImport_Key.setObjectName("actionImport_Key")
        self.menuHelp.addAction(self.actionRead_me)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Key)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoApp_V1.09"))
        self.pushButtonEnFolder.setText(_translate("MainWindow", "Select Folder"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> If you do not have a key, you can use the \'KEY GENERATOR\' to generate a new key!</p><p>The key is required for the <span style=\" font-weight:600;\">RSA</span> algorithm! (<span style=\" font-weight:600;\">RSA</span> uses asymmetric keys (Public Key: *.pubk), <span style=\" font-weight:600;\">AES</span> and <span style=\" font-weight:600;\">TripleDES</span> use symmetric keys!)</p></body></html>"))
        self.pushButtonEnCreate.setText(_translate("MainWindow", "CREATE KEY!"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Note: </span>With algorithm RSA, File must not be too large!(&lt; 1MB). Use select folder if you want to encrypt all files in the folder! </p><p><span style=\" font-weight:600;\">Note:</span> Only encrypt files in current directory! Do not encrypt files in subfolders.</p></body></html>"))
        self.radioEnAES.setText(_translate("MainWindow", "AES"))
        self.checkBoxEnSource.setText(_translate("MainWindow", "Use Source folder as Output folder!"))
        self.pushButtonEnKey.setText(_translate("MainWindow", "Import Key"))
        self.label_2.setText(_translate("MainWindow", "PlainText/Source Patch:"))
        self.radioEn3DES.setText(_translate("MainWindow", "TripleDES"))
        self.radioEnRSA.setText(_translate("MainWindow", "RSA"))
        self.label.setText(_translate("MainWindow", "Algorithm:"))
        self.label_4.setText(_translate("MainWindow", "CipherText/Output folder:"))
        self.label_5.setText(_translate("MainWindow", "Proccess:"))
        self.label_3.setText(_translate("MainWindow", "Password/Key File Path:"))
        self.pushButtonEnOut.setText(_translate("MainWindow", "Select Folder"))
        self.pushButtonEnFile.setText(_translate("MainWindow", "Select File"))
        self.pushButtonEnStart.setText(_translate("MainWindow", "START ENCRYPT"))
        self.checkBoxEnDelete.setText(_translate("MainWindow", "Delete Source File!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_encrypt), _translate("MainWindow", "ENCRYPT"))
        self.label_11.setText(_translate("MainWindow", "PlainText/Output folder:"))
        self.pushButtonDeFolder.setText(_translate("MainWindow", "Select Folder"))
        self.pushButtonDeFile.setText(_translate("MainWindow", "Select File"))
        self.pushButtonDeKey.setText(_translate("MainWindow", "Import Key"))
        self.pushButtonDeOut.setText(_translate("MainWindow", "Select Folder"))
        self.pushButtonDeStart.setText(_translate("MainWindow", "START DECRYPT"))
        self.radioButtonDeAES.setText(_translate("MainWindow", "AES"))
        self.label_9.setText(_translate("MainWindow", "CipherText/Source Patch:"))
        self.radioButtonDe3DES.setText(_translate("MainWindow", "TripleDES"))
        self.label_12.setText(_translate("MainWindow", "Process:"))
        self.label_8.setText(_translate("MainWindow", "Algorithm:"))
        self.radioButtonDeRSA.setText(_translate("MainWindow", "RSA"))
        self.label_10.setText(_translate("MainWindow", "Password/Key File Path:"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> RSA uses asymmetric keys (Private Key: *.prvk), AES and Triple DES use symmetric keys!</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Use select folder if you want to decrypt all files in the folder! </p><p><span style=\" font-weight:600;\">Note:</span> Only decrypt files in current directory! Do not decrypt files in subfolders.</p></body></html>"))
        self.checkBoxDeSource.setText(_translate("MainWindow", "Use Source folder as Output folder!"))
        self.checkBoxDeDelete.setText(_translate("MainWindow", "Delete Source File!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_decrypt), _translate("MainWindow", "DECRYPTION"))
        self.label_18.setText(_translate("MainWindow", "Key Length (number):"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa7f;\">Key:</span></p></body></html>"))
        self.pushButtonSymCopy.setText(_translate("MainWindow", "Copy to Clipboard"))
        self.pushButtonSymGenerate.setText(_translate("MainWindow", "Generate"))
        self.pushButtonSymSave.setText(_translate("MainWindow", "Save Key To File"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSym), _translate("MainWindow", "Symmetric Key"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">Key Size:</span></p></body></html>"))
        self.pushButtonAsymGenerate.setText(_translate("MainWindow", "Generate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabAsym), _translate("MainWindow", "Asymmetric Key"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_generator), _translate("MainWindow", "KEY GENERATOR"))
        self.label_16.setText(_translate("MainWindow", "Hash Code/Original File:"))
        self.pushButtonHashVerify.setText(_translate("MainWindow", "VERIFY"))
        self.pushButtonHashFile2.setText(_translate("MainWindow", "Select File"))
        self.pushButtonHashFile1.setText(_translate("MainWindow", "Select File"))
        self.label_17.setText(_translate("MainWindow", "Decrypted File:"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#55ff00;\">SHA-256</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hash), _translate("MainWindow", "HASH (SHA256)"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File(encrypt/decrypt)"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder(encrypt/decrypt)"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionRead_me.setText(_translate("MainWindow", "Read me!"))
        self.actionImport_Key.setText(_translate("MainWindow", "Import Key"))
        self.comboBoxAsym.addItems(['1024','2048 (Recommended)','3072','4096'])
        self.actionRead_me.triggered.connect(self.readMeMessage)

        #MENU FILE
        self.actionOpen_File.triggered.connect(self.getPathFileMenu)
        self.actionOpen_Folder.triggered.connect(self.getPathFolderMenu)
        self.actionImport_Key.triggered.connect(self.getPathFileKeyMenu)
        #ENCRYPT TAB
        self.pushButtonEnCreate.clicked.connect(self.switchToGenerateTab)
        self.pushButtonEnFile.clicked.connect(lambda: self.getPathFile(self.lineEditEnSource))
        self.pushButtonEnFolder.clicked.connect(lambda: self.getPathFolder(self.lineEditEnSource))
        self.pushButtonEnKey.clicked.connect(lambda: self.getPathFile(self.lineEditEnKey, True))
        self.pushButtonEnOut.clicked.connect(lambda: self.getPathFolder(self.lineEditEnOut))
        self.pushButtonEnStart.clicked.connect(self.startEncrypt)
        self.lineEditEnSource.textChanged.connect(self.outFolowSource)
        self.checkBoxEnSource.stateChanged.connect(self.outFolowSource)
        #DECRYPT TAB
        self.pushButtonDeFile.clicked.connect(lambda: self.getPathFile(self.lineEditDeSource, False, False))
        self.pushButtonDeFolder.clicked.connect(lambda: self.getPathFolder(self.lineEditDeSource))
        self.pushButtonDeKey.clicked.connect(lambda: self.getPathFile(self.lineEditDeKey, True, False))
        self.pushButtonDeOut.clicked.connect(lambda: self.getPathFolder(self.lineEditDeOut))
        self.pushButtonDeStart.clicked.connect(self.startDecrypt)
        self.lineEditDeSource.textChanged.connect(self.outFolowSource)
        self.checkBoxDeSource.stateChanged.connect(self.outFolowSource)
        #GENERATOR TAB
            # Symmetric Keys
        self.pushButtonSymSave.clicked.connect(self.saveFileKeySym)
        self.pushButtonSymGenerate.clicked.connect(self.generateSymKey)
        self.pushButtonSymCopy.clicked.connect(self.copyToClipBoard)
            # Asymmetric Keys
        self.pushButtonAsymGenerate.clicked.connect(self.generateASymKey)
        #HASH TAB
        self.pushButtonHashFile1.clicked.connect(lambda: self.getPathFile(self.lineEditHash1))
        self.pushButtonHashFile2.clicked.connect(lambda: self.getPathFile(self.lineEditHash2))
        self.pushButtonHashVerify.clicked.connect(self.verify)

    def outFolowSource(self):
        if(self.tabWidget.currentIndex() == 0):
            if(self.checkBoxEnSource.isChecked()):
                self.lineEditEnOut.setText(proccess.getpathFolder(self.lineEditEnSource.text()))
        else:
            if(self.checkBoxDeSource.isChecked()):
                self.lineEditDeOut.setText(proccess.getpathFolder(self.lineEditDeSource.text())) 

    def switchToGenerateTab(self):
        self.tabWidget.setCurrentIndex(2)

    def readMeMessage(self):
        QMessageBox.about(self.centralwidget,"READ ME!","Author: Nguyen Van Son.\nVersion: V1.09.\nDescription: The tool is used to encrypt files or folders according to basic standards such as RSA, AES, TripleDES. It is also a tool for checking files (hash).")

    def clearAll(self):
        self.lineEditEnSource.setText('')
        self.lineEditEnKey.setText('')
        self.lineEditEnOut.setText('')

    def copyToClipBoard(self):
        string_ = self.lineEditSymKey.text()
        if(string_ == ''):
            QMessageBox.warning(self.centralwidget, "Warning:", "No content to copy!")
        else:
            cb = QtWidgets.QApplication.clipboard()
            cb.clear(mode=cb.Clipboard )
            cb.setText(string_, mode=cb.Clipboard)
            QMessageBox.information(self.centralwidget,"Notification:", "Copied to Clipboard!")

    def getPathFile(self, LineEdit, key=False, encrypt= True):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if(encrypt):
            if(key):
                dialog.setNameFilters(["Text files (*.txt)", "Public Key Files (*.pubk)"])
        else:
            if(key):
                dialog.setNameFilters(["Text files (*.txt)", "Private Key Files (*.prvk)"])
            else:
                dialog.setNameFilters(["Cipher files (*.cipher)"])

        if dialog.exec():
            pathfile = dialog.selectedFiles()
            LineEdit.setText(pathfile[0])

    def getPathFolder(self, LineEdit):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec():
            pathfolder = dialog.selectedFiles()
            LineEdit.setText(pathfolder[0])

    def getPathFileMenu(self):
        currentTab = self.tabWidget.currentIndex()
        if(currentTab != 0 and currentTab != 1):
            QMessageBox.warning(self.centralwidget, "Warning:", "This function is only used for tab ENCRYPT and tab DECRYPT!")
            return

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec():
            pathfile = dialog.selectedFiles()
            # LineEdit.setText(pathfile[0])
            if(currentTab == 0):
                self.lineEditEnSource.setText(pathfile[0])
            else:
                self.lineEditDeSource.setText(pathfile[0])

    def getPathFileKeyMenu(self):
        currentTab = self.tabWidget.currentIndex()
        if(currentTab != 0 and currentTab != 1):
            QMessageBox.warning(self.centralwidget, "Warning:", "This function is only used for tab ENCRYPT and tab DECRYPT!")
            return

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if(currentTab == 0):
            dialog.setNameFilters(["Text files (*.txt)", "Public Key Files (*.pubk)"])
        else:
            dialog.setNameFilters(["Text files (*.txt)", "Private Key Files (*.prvk)"])

        if dialog.exec():
            pathfile = dialog.selectedFiles()
            # LineEdit.setText(pathfile[0])
            if(currentTab ==0):
                self.lineEditEnKey.setText(pathfile[0])
            else:
                self.lineEditDeKey.setText(pathfile[0])

    def getPathFolderMenu(self):
        currentTab = self.tabWidget.currentIndex()
        if(currentTab != 0 and currentTab != 1):
            QMessageBox.warning(self.centralwidget, "Warning:", "This function is only used for tab ENCRYPT and tab DECRYPT!")
            return
        
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)

        if dialog.exec():
            pathfile = dialog.selectedFiles()
            # LineEdit.setText(pathfile[0])
            if(currentTab ==0):
                self.lineEditEnSource.setText(pathfile[0])
                self.lineEditEnOut.setText(pathfile[0])
            else:
                self.lineEditDeSource.setText(pathfile[0])
                self.lineEditDeOut.setText(pathfile[0])
    # ENCRYPT
    def startEncrypt(self):
        # print(self.lineEditEnSource.text())
        self.progressBarEn.setProperty("value", 0)
        if(proccess.checkPathEncryptOrDecrypt(self.lineEditEnSource.text(), self.lineEditEnOut.text())):
            key_ = self.lineEditEnKey.text()
            if self.radioEnAES.isChecked():
                if(proccess.checkKey(key_)):
                    self.progressBarEn.setProperty("value", 10)
                    proccess.encryptAES(self.lineEditEnSource.text(),key_,self.lineEditEnOut.text(),self.progressBarEn, self.checkBoxEnDelete.isChecked())
                    self.progressBarEn.setProperty("value", 100)
                    QMessageBox.information(self.centralwidget,"Notification","Encrypt Successfull!")
                else:
                    QMessageBox.critical(self.centralwidget,"Error:","The file type of file Key does not match the algorithm selected!")
            elif self.radioEnRSA.isChecked():
                if(proccess.checkKey(key_,True,True)):
                    self.progressBarEn.setProperty("value", 10)
                    try:
                        proccess.encryptRSA(self.lineEditEnSource.text(),key_,self.lineEditEnOut.text(),self.progressBarEn, self.checkBoxEnDelete.isChecked())
                        self.progressBarEn.setProperty("value", 100)
                        QMessageBox.information(self.centralwidget,"Notification","Encrypt Successfull!")
                    except ValueError:
                        QMessageBox.critical(self.centralwidget,"Error:","RSA Algorithms: This size of currnet file is to big!")
                else:
                    QMessageBox.critical(self.centralwidget,"Error:","The file type of file Key does not match the algorithm selected!")
            elif self.radioEn3DES.isChecked():
                if(proccess.checkKey(key_)):
                    self.progressBarEn.setProperty("value", 10)
                    proccess.encrypt3DES(self.lineEditEnSource.text(),key_,self.lineEditEnOut.text(),self.progressBarEn, self.checkBoxEnDelete.isChecked())
                    self.progressBarEn.setProperty("value", 100)
                    QMessageBox.information(self.centralwidget,"Notification","Encrypt Successfull!")
                else:
                    QMessageBox.critical(self.centralwidget,"Error:","The file type of file Key does not match the algorithm selected!")
            else:
                QMessageBox.warning(self.centralwidget,"Warning:","You need to choose an algorithm!")
        else:
            QMessageBox.critical(self.centralwidget,"Error:","The paths are not correct!. Please check again!")

    # DECRYPT
    def startDecrypt(self):
        self.progressBarDe.setProperty("value", 0)
        if(proccess.checkPathEncryptOrDecrypt(self.lineEditDeSource.text(), self.lineEditDeOut.text())):
            key_ = self.lineEditDeKey.text()
            if self.radioButtonDeAES.isChecked():
                if(proccess.checkKey(key_,False)):
                    self.progressBarDe.setProperty("value", 10)
                    check = proccess.decryptAES(self.lineEditDeSource.text(),key_,self.lineEditDeOut.text(),self.progressBarDe,self.checkBoxDeDelete.isChecked())
                    self.progressBarDe.setProperty("value", 100)
                    if(check):
                        QMessageBox.information(self.centralwidget,"Notification","Decrypt Successfull!")
                    else:
                        QMessageBox.warning(self.centralwidget,"Warning:","Decrypt file success, hash value is incorrect. This is not origin file!")
                else:
                    QMessageBox.critical(self.centralwidget,"Error:","The file type of file Key does not match the algorithm selected!")
            elif self.radioButtonDeRSA.isChecked():
                if(proccess.checkKey(key_,False,True)):
                    self.progressBarDe.setProperty("value", 10)
                    try:
                        check = proccess.decryptRSA(self.lineEditDeSource.text(),key_,self.lineEditDeOut.text(),self.progressBarDe,self.checkBoxDeDelete.isChecked())
                        self.progressBarDe.setProperty("value", 100)
                        if(check):
                            QMessageBox.information(self.centralwidget,"Notification","Decrypt Successfull!")
                        else:
                            QMessageBox.warning(self.centralwidget,"Warning:","Decrypt file success, hash value is incorrect. This is not origin file!")
                    except ValueError:
                        QMessageBox.critical(self.centralwidget,"Error:","RSA Algorithms: This size of currnet file is to big!")
                else:
                    QMessageBox.critical(self.centralwidget,"Error:","The file type of file Key does not match the algorithm selected!")
            elif self.radioButtonDe3DES.isChecked():
                if(proccess.checkKey(key_,False)):
                    self.progressBarDe.setProperty("value", 10)
                    check = proccess.decrypt3DES(self.lineEditDeSource.text(),key_,self.lineEditDeOut.text(),self.progressBarDe,self.checkBoxDeDelete.isChecked())
                    self.progressBarDe.setProperty("value", 100)
                    if(check):
                        QMessageBox.information(self.centralwidget,"Notification","Decrypt Successfull!")
                    else:
                        QMessageBox.warning(self.centralwidget,"Warning:","Decrypt file success, hash value is incorrect. This is not origin file!")
                else:
                    QMessageBox.critical(self.centralwidget,"Error:","The file type of file Key does not match the algorithm selected!")
            else:
                QMessageBox.warning(self.centralwidget,"Warning:","You need to choose an algorithm!")
        else:
            QMessageBox.critical(self.centralwidget,"Error:","The paths are not correct!. Please check again!")

    # def decryptAESFile(self):
        
    # def decrypt3DESFile(self):

    # def decryptRSAFile(self):

    # def decryptAESFolder(self):

    # def decrypt3DESFolder(self):

    # def decryptRSAFolder(self):
    # GENERATOR
    def saveFileKeySym(self):
        key = self.lineEditSymKey.text()
        if(key == ''):
            QMessageBox.warning(self.centralwidget, "Warning:", "Key hasn't been created!")
            return
        str = QFileDialog().getSaveFileName(self.centralwidget,"Save file: ","","Text files (*.txt)")[0]
        # print(str)
        if(str != ''):
            proccess.saveFile(str,key)
            QMessageBox.information(self.centralwidget,"Notification","The key has been saved to the file!")
    
    def generateSymKey(self):
        length = self.lineEditSymLength.text()
        if(length == '' or not length.isnumeric()):
            QMessageBox.warning(self.centralwidget,"Warning:","You need to fill in a positive integer!")
        else:
            self.lineEditSymKey.setText(proccess.generateSymmetricKey(length))

    def generateASymKey(self):
        # print(self.comboBoxAsym.currentText())
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setWindowTitle('Select Folder to save pair key: ')
        if dialog.exec():
            pathFolder = dialog.selectedFiles()[0]
            # print(pathFolder + '\\')
            try:
                proccess.generateAsymmetricKey(self.comboBoxAsym.currentText(),pathFolder)
                QMessageBox.information(self.centralwidget,"Notification:", "Generate public key and private key successful!")
            except:
                QMessageBox.critical(self.centralwidget,"Error:","An error occurred! Please check and try again!")

    # HASH
    def verify(self):
        path1 = self.lineEditHash1.text()
        path2 = self.lineEditHash2.text()
        if (proccess.checkPathFileOrFolder(path2)):
            hash1 = ''
            hash2 = ''
            if(proccess.checkPathFileOrFolder(path1)):
                hash1 = proccess.hashSha256(path1)
                hash2 = proccess.hashSha256(path2)
            else:
                hash1 = path1
                hash2 = proccess.hashSha256(path2)

            if(hash1 == hash2):
                cb = QtWidgets.QApplication.clipboard()
                cb.clear(mode=cb.Clipboard)
                cb.setText(hash1, mode=cb.Clipboard)
                QMessageBox.information(self.centralwidget,"Verify!","The Hash Codes Match!\nHash Code: " + hash2 + "\nThe hash code has been copied to the clipboard!")
            else:
                QMessageBox.warning(self.centralwidget,"Verify!","The Hash Codes Do Not Match!\nHash Code1: " + hash1 +"\nHash Code2: "+ hash2)
        else:
            QMessageBox.critical(self.centralwidget,"Error:","The file path is incorrect. Please check again!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
