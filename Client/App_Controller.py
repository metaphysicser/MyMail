"""
-*- coding: utf-8 -*-
@Time    : 2022/1/3 18:05
@Author  : 夕照深雨
@File    : App_Controller.py
@Software: PyCharm

Attention：

"""
import sys
from imaplib import Int2AP
import random

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtGui
from PyQt5 import QtGui, QtWidgets
from Client.App_view.View.Login_View import Login_View
from Client.App_view.View.main import Ui_MainWindow
from Client.Model.App_Model import App_Model


class App_Controller:
    def __init__(self):

        self._app = QApplication(sys.argv)
        self._view = Login_View()
        self._model = App_Model()
        self.focus = None
        self.init()

    def init(self):
        self._view.quit_signal.connect(QCoreApplication.instance().quit)  # 退出按钮
        self._view.login_signal.connect(self.login)  # 登陆按钮

    def main_init(self):
        self._view.label_4.setText(self.username)  # 获得用户名
        if self.email is not None:
            self._view.comboBox.addItems(self.email)
            self.current_email = self._view.comboBox.currentText()  # 获得用户已有邮箱
        self._view.write_mail.connect(self.write_mail)
        self._view.receive_mail.connect(self.receive_mail)
        self._view.address_book.connect(self.address_book)
        self._view.sent_mail.connect(self.sent_mail)
        self._view.trash_bin.connect(self.trash_bin)
        self._view.draft_box.connect(self.draft_box)

    def login(self):
        """
        点击登录按钮
        Returns:

        """
        username = self._view.lineEdit.text()
        password = self._view.lineEdit_2.text()
        res = self._model.login(username, password)  # 得到的结果
        QtWidgets.QMessageBox.warning(self._view, "提示", res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        if res["action"] == "login_response" and res["content"]["status"] == "True":  # 登陆成功
            self.username = username
            self.email = res["content"]["account"]
            main_window = Ui_MainWindow()
            self._view.close()
            self._view = main_window
            self.main_init()
            self._view.show()
        elif res["content"]["status"] == "False":  # 登陆失败
            pass

    def restore_style(self):
        if self.focus is None:
            pass
        if self.focus is self._view.pushButton_2:
            self.write_mail_normal()
        if self.focus is self._view.pushButton_3:
            self.receive_mail_normal()
        if self.focus is self._view.pushButton_4:
            self.address_book_normal()
        if self.focus is self._view.pushButton_5:
            self.sent_mail_normal()
        if self.focus is self._view.pushButton_6:
            self.trash_bin_normal()
        if self.focus is self._view.pushButton_7:
            self.draft_box_normal()
    def write_mail(self):
        self.restore_style()
        self.focus = self._view.pushButton_2
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/写邮件_按下.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_2.setIcon(icon)
        self._view.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    color: rgbrgb(0, 170, 255);\n"
                                        "background-color: rgb(241, 241, 241);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 30px;\n"
                                        "    border-color: rgb(2, 194, 18);\n"
                                        "    \n"
                                        "\n"
                                        "\n"
                                        "}\n")
    def write_mail_normal(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/写邮件_平时.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_2.setIcon(icon)
        self._view.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(10, 2, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 30px;\n"
"    border-color: rgb(2, 194, 18);\n"
"    \n"
"\n"
"\n"
"}\n"
"\n")



    def receive_mail(self):
        self.restore_style()
        self.focus = self._view.pushButton_3
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/收件箱_按下.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_3.setIcon(icon)
        self._view.pushButton_3.setStyleSheet("QPushButton{\n"
                                              "color: rgb(255, 255, 255);\n"
                                               "background-color: rgb(220, 0, 0);\n"
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")
    def receive_mail_normal(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/收件箱.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_3.setIcon(icon)
        self._view.pushButton_3.setStyleSheet("QPushButton{\n"
                                             
                                               "background-color: rgb(255, 255, 255);\n"
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")
    def address_book(self):
        self.restore_style()
        self.focus = self._view.pushButton_4
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/通讯录_按下.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_4.setIcon(icon)
        self._view.pushButton_4.setStyleSheet("QPushButton{\n"
                                              "color: rgb(255, 255, 255);\n"
                                             " background-color: rgb(235, 235, 0);\n "
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")

    def address_book_normal(self):
        self.focus = self._view.pushButton_4
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/通讯录.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_4.setIcon(icon)
        self._view.pushButton_4.setStyleSheet("QPushButton{\n"
                                             
                                              "background-color: white;;\n"
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")
    def sent_mail(self):
        self.restore_style()
        self.focus = self._view.pushButton_5
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/已发送_按下.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_5.setIcon(icon)
        self._view.pushButton_5.setStyleSheet("QPushButton{\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color:rgb(0, 170, 255);\n "
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")

    def sent_mail_normal(self):
        self.focus = self._view.pushButton_5
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/已发送_平时.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_5.setIcon(icon)
        self._view.pushButton_5.setStyleSheet("QPushButton{\n"

                                              "background-color: white;;\n"
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")
    def trash_bin(self):
        self.restore_style()
        self.focus = self._view.pushButton_6
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/垃圾箱_按下.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_6.setIcon(icon)
        self._view.pushButton_6.setStyleSheet("QPushButton{\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color:rgb(0, 170, 255);\n "
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")

    def trash_bin_normal(self):
        self.focus = self._view.pushButton_6
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/垃圾箱_平时.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_6.setIcon(icon)
        self._view.pushButton_6.setStyleSheet("QPushButton{\n"

                                              "background-color: white;;\n"
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")
    def draft_box(self):
        self.restore_style()
        self.focus = self._view.pushButton_7
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/草稿箱_按下.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_7.setIcon(icon)
        self._view.pushButton_7.setStyleSheet("QPushButton{\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color:rgb(0, 170, 255);\n "
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")
    def draft_box_normal(self):
        self.focus = self._view.pushButton_7
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/草稿箱_平时.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._view.pushButton_7.setIcon(icon)
        self._view.pushButton_7.setStyleSheet("QPushButton{\n"

                                              "background-color: white;;\n"
                                              "    border-style: outset;\n"
                                              "    border-width: 0px;\n"
                                              "    border-radius: 30px;\n"
                                              "    border-color: rgb(2, 194, 18);\n"
                                              "    \n"
                                              "\n"
                                              "\n"
                                              "}\n")

    def run(self):
        self._view.show()
        return self._app.exec_()


if __name__ == '__main__':
    c = App_Controller()  # 调用控制器
    sys.exit(c.run())
