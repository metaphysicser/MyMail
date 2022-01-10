# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
import Client.App_view.resource_rc
from Client.App_view.View.Window import Window


class Login_View(Window):
    quit_signal = QtCore.pyqtSignal()
    login_signal = QtCore.pyqtSignal()
    register_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(Login_View, self).__init__(parent)
        self.setupUi(self)
        self.connect_signal()

    def connect_signal(self):
        self.pushButton.clicked.connect(self.quit_signal)
        self.pushButton_3.clicked.connect(self.login_signal)
        self.pushButton_2.clicked.connect(self.register_signal)

    def setupUi(self, Form):
        self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        Form.setObjectName("Form")
        Form.resize(647, 438)
        Form.setMinimumSize(QtCore.QSize(647, 438))
        Form.setMaximumSize(QtCore.QSize(647, 438))
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(-10, 0, 661, 451))
        self.listView.setStyleSheet("background-image: url(:/newPrefix/img/登陆背景图.png);")
        self.listView.setObjectName("listView")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 581, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 200, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(150, 20, 100, 20)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 313, 654, 97))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 350, 652, 106))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(50, 20, 100, 40)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
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
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(61, 74, 255);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed{\n"
"   background-color:rgb(61, 74, 255);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:rgb(84, 42, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
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
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "密码"))
        self.pushButton_2.setText(_translate("Form", "注册"))
        self.pushButton_3.setText(_translate("Form", "登录"))
        self.pushButton.setText(_translate("Form", "退出"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login_View()
    window.show()
    sys.exit(app.exec_())
