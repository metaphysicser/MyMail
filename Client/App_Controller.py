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

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from Client.App_view.Login_view.Login_View import Login_View
from Client.Model.App_Model import App_Model


class App_Controller:
    def __init__(self):
        self._app = QApplication(sys.argv)
        self._view = Login_View()
        self._model = App_Model()
        self.init()

    def init(self):
        self._view.quit_signal.connect(QCoreApplication.instance().quit)  # 退出按钮
        self._view.login_signal.connect(self.login)  # 登陆按钮

    def login(self):
        """
        点击登录按钮
        Returns:

        """
        username = self._view.lineEdit.text()
        password = self._view.lineEdit_2.text()
        res = self._model.login(username, password)  # 得到的结果
        print(res)
        QtWidgets.QMessageBox.warning(self._view, "提示", res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        if res["action"] == "login_response" and res["content"]["status"] == "True":  # 登陆成功
            pass
        elif res["content"]["status"] == "False":  # 登陆失败
            pass

    def run(self):
        self._view.show()
        return self._app.exec_()


if __name__ == '__main__':
    c = App_Controller()  # 调用控制器
    sys.exit(c.run())
