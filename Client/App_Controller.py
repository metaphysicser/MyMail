"""
-*- coding: utf-8 -*-
@Time    : 2022/1/3 18:05
@Author  : 夕照深雨
@File    : App_Controller.py
@Software: PyCharm

Attention：

"""
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from Client.App_Model import App_Model
from Client.App_view.Login.Login_view import Login_View


class App_Controller:
    def __init__(self):
        self._app = QApplication(sys.argv)
        self._view = Login_View()
        self._model = App_Model()
        self.init()

    def init(self):
        self._view.quit_signal.connect(QCoreApplication.instance().quit)

    def run(self):
        self._view.show()
        return self._app.exec_()

if __name__ == '__main__':
    c = App_Controller()  # 调用控制器
    sys.exit(c.run())