"""
-*- coding: utf-8 -*-
@Time    : 2022/1/3 18:05
@Author  : 夕照深雨
@File    : App_Controller.py
@Software: PyCharm

Attention：

"""
import base64
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtGui
from PyQt5 import QtGui, QtWidgets
from Client.App_view.View.Login_View import Login_View
from Client.App_view.View.add_account import Add_account_View
from Client.App_view.View.main import Ui_MainWindow
from Client.App_view.View.read_email import Read_Form
from Client.App_view.View.register import Register_View
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
        self._view.register_signal.connect(self.register_open)

    def register_init(self):
        self._sub_view.register_signal.connect(self.register)  # 退出按钮
        self._sub_view.quit_signal.connect(self.reg_close)

    def add_account_init(self):
        self._sub_view.add_signal.connect(self.add_)  # 退出按钮
        self._sub_view.quit_signal.connect(self.reg_close)

    def reg_close(self):
        self._sub_view.close()

    def add_(self):
        account = self._sub_view.lineEdit.text()
        password = self._sub_view.lineEdit_2.text()
        res = self._model.add_account(self.username, password, account)
        QtWidgets.QMessageBox.warning(self._view, "提示", res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        self.email.append(account)

        self._view.comboBox.addItems(self.email)
        self.current_email = self._view.comboBox.currentText()




    def main_init(self):
        self._view.label_4.setText(self.username)  # 获得用户名

        self._view.comboBox.addItems(self.email)
        self.current_email = self._view.comboBox.currentText()  # 获得用户已有邮箱
        self._view.write_mail.connect(self.write_mail)
        self._view.receive_mail.connect(self.receive_mail)
        self._view.address_book.connect(self.address_book)
        self._view.sent_mail.connect(self.sent_mail)
        self._view.trash_bin.connect(self.trash_bin)
        self._view.draft_box.connect(self.draft_box)
        self._view.add_account.connect(self.add_account)
        self._sub_view = self._view.form1
        self.write_mail_init()


    def write_mail_init(self):
        self._sub_view.send_signal.connect(self.send_mail)
        self._sub_view.save_signal.connect(self.save_mail)

    def register(self):
        username = self._sub_view.lineEdit.text()
        password = self._sub_view.lineEdit_2.text()
        res = self._model.register(username, password)
        QtWidgets.QMessageBox.warning(self._view, "提示", res["content"]["reason"], QtWidgets.QMessageBox.Cancel)

    def add_account(self):
        add_account_window = Add_account_View()
        self._sub_view = add_account_window
        self.add_account_init()
        self._sub_view.show()

    def register_open(self):
        """
        注册
        Returns:

        """
        register_window = Register_View()
        self._sub_view = register_window
        self.register_init()
        self._sub_view.show()


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
            self.email = [] if res["content"]["account"] is None else res["content"]["account"]
            main_window = Ui_MainWindow()
            self._view.close()
            self._view = main_window
            self.main_init()
            self._view.show()
        elif res["content"]["status"] == "False":  # 登陆失败
            pass



    def send_mail(self):
        sender = self._view.comboBox.currentText()
        sender_name = self._sub_view.lineEdit.text()
        receiver = self._sub_view.lineEdit.text()
        title = self._sub_view.lineEdit_2.text()
        text = self._sub_view.textEdit.toPlainText()
        file= self._sub_view.comboBox.file
        res = self._model.send_email(sender, sender_name,receiver, title, text, file, "sent")
        QtWidgets.QMessageBox.warning(self._view, "提示", res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        if res["content"]["status"] == "True":
            self._sub_view.lineEdit.clear()
            self._sub_view.lineEdit_2.clear()
            self._sub_view.textEdit.clear()



    def save_mail(self):
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



        self._sub_view = self._view.form1
        self.write_mail_init()
        self._view.qsl.setCurrentIndex(0)

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

        self._sub_view = self._view.form2
        self._view.qsl.setCurrentIndex(1)

        account = self._view.comboBox.currentText()
        self.res = self._model.receive_mail(account, "Inbox")
        if self.res["content"]["status"] == "False":
            QtWidgets.QMessageBox.warning(self._view, "提示", self.res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        else:

            self.mail_index = list(self.res["content"]["mail"].keys())
            mail = self.res["content"]["mail"]
            self._sub_view.dmodel.clear()
            self._sub_view.show_mail(mail)
            self._view.qsl.setCurrentIndex(1)

            self._sub_view.look_signal.connect(self.look_mail)

    def look_mail(self):
        num = self._sub_view.listView.currentIndex().row()
        mail_num = self.mail_index[num]
        mail_content = self.res["content"]["mail"][str(mail_num)]
        subject = mail_content["subject"]
        body = mail_content["body"]

        html = mail_content["html"]
        if html is not None:
            html = base64.b64decode(html)
            html = str(html, encoding='utf8')
        from_ = mail_content["from"][1]


        read_window = Read_Form()
        read_window.show_mail(from_, subject, html if html is not None else body)
        read_window.show()




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
        self._sub_view = self._view.form2
        self._view.qsl.setCurrentIndex(1)

        account = self._view.comboBox.currentText()
        self.res = self._model.receive_mail(account, "Sent")
        if self.res["content"]["status"] == "False":
            QtWidgets.QMessageBox.warning(self._view, "提示", self.res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        else:

            self.mail_index = list(self.res["content"]["mail"].keys())
            mail = self.res["content"]["mail"]
            self._sub_view.dmodel.clear()
            self._sub_view.show_mail(mail)
            self._view.qsl.setCurrentIndex(1)

            self._sub_view.look_signal.connect(self.look_mail)

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

        self._sub_view = self._view.form2
        self._view.qsl.setCurrentIndex(1)

        account = self._view.comboBox.currentText()
        self.res = self._model.receive_mail(account, "Junk")
        if self.res["content"]["status"] == "False":
            QtWidgets.QMessageBox.warning(self._view, "提示", self.res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        else:

            self.mail_index = list(self.res["content"]["mail"].keys())
            mail = self.res["content"]["mail"]
            self._sub_view.dmodel.clear()
            self._sub_view.show_mail(mail)
            self._view.qsl.setCurrentIndex(1)

            self._sub_view.look_signal.connect(self.look_mail)

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
        self._sub_view = self._view.form2
        self._view.qsl.setCurrentIndex(1)

        account = self._view.comboBox.currentText()
        self.res = self._model.receive_mail(account, "Drafts")
        if self.res["content"]["status"] == "False":
            QtWidgets.QMessageBox.warning(self._view, "提示", self.res["content"]["reason"], QtWidgets.QMessageBox.Cancel)
        else:

            self.mail_index = list(self.res["content"]["mail"].keys())
            mail = self.res["content"]["mail"]
            self._sub_view.dmodel.clear()
            self._sub_view.show_mail(mail)
            self._view.qsl.setCurrentIndex(1)

            self._sub_view.look_signal.connect(self.look_mail)
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
