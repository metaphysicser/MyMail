"""
-*- coding: utf-8 -*-
@Time    : 2022/1/10 23:56
@Author  : 夕照深雨
@File    : add_account.py
@Software: PyCharm

Attention：

"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
import Client.App_view.resource_rc
from Client.App_view.View.CircleLineWindow import CircleLineWindow


class Add_account_View(CircleLineWindow):
    add_signal = QtCore.pyqtSignal()
    quit_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(Add_account_View, self).__init__(parent)
        self.setupUi(self)
        self.connect_signal()


    def connect_signal(self):
        self.pushButton.clicked.connect(self.quit_signal)
        self.pushButton_2.clicked.connect(self.add_signal)

    def setupUi(self, Form):
        # self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        Form.setObjectName("Form")
        Form.resize(488, 300)
        Form.setMinimumSize(QtCore.QSize(488, 300))
        Form.setMaximumSize(QtCore.QSize(488, 300))
        Form.setObjectName("Form")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 70, 329, 34))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color: transparent;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color:grey;\n"
"border:0px;\n"
"border-bottom: 2px solid #B3B3B3;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-bottom: 3px solid #66A3FF;    \n"
"    }\n"
"\n"
"QLineEdit:focus{\n"
"    border-bottom: 3px solid #E680BD;    #下框线变为3px像素宽度，颜色为#E680BD\n"
"    }")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 140, 329, 34))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"background-color: transparent;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color:grey;\n"
"border:0px;\n"
"border-bottom: 2px solid #B3B3B3;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-bottom: 3px solid #66A3FF;    \n"
"    }\n"
"\n"
"QLineEdit:focus{\n"
"    border-bottom: 3px solid #E680BD;    #下框线变为3px像素宽度，颜色为#E680BD\n"
"    }")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 220, 134, 42))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(29, 70, 255);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color: white\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"   background-color: rgb(29, 70, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"   background-color:rgb(84, 42, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 220, 134, 42))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(10, 10, 185);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed{\n"
"   background-color:rgb(10, 10, 185);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:rgb(84, 42, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "邮箱账号"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "密码"))
        self.pushButton_2.setText(_translate("Form", "添加"))
        self.pushButton.setText(_translate("Form", "退出"))

