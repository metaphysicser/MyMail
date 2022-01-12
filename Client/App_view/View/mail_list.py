import string
from random import choice, randint
from time import time

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    from PyQt5.QtCore import QSortFilterProxyModel, Qt, QSize
    from PyQt5.QtGui import QStandardItem, QStandardItemModel
    from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListView, \
        QHBoxLayout, QLineEdit, QApplication
except ImportError:
    from PySide2.QtCore import QSortFilterProxyModel, Qt, QSize
    from PySide2.QtGui import QStandardItem, QStandardItemModel
    from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListView, \
        QHBoxLayout, QLineEdit, QApplication


def randomChar(y):
    # 返回随机字符串
    return ''.join(choice(string.ascii_letters) for _ in range(y))


class CustomWidget(QWidget):

    def __init__(self, text, *args, **kwargs):
        super(CustomWidget, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        line = QLineEdit(text,self)
        line.setStyleSheet("QLineEdit{\n"
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
        line.setText("")

        line.setDisabled(True)

        layout.addWidget(line)

        # button = QPushButton('查看', self)
        #
        # button.setStyleSheet("QPushButton{\n"
        #                                 "    background-color: rgb(29, 70, 255);\n"
        #                                 "    border-style: outset;\n"
        #                                 "    border-width: 0px;\n"
        #                                 "    border-radius: 10px;\n"
        #                                 "    border-color: beige;\n"
        #                                 "    min-width: 4em;\n"
        #                                 "    padding: 6px;\n"
        #                                 "    color: white\n"
        #                                 "}\n"
        #                                 "\n"
        #                                 "\n"
        #                                 "QPushButton:pressed{\n"
        #                                 "   background-color: rgb(29, 70, 255);\n"
        #                                 "}\n"
        #                                 "\n"
        #                                 "\n"
        #                                 "QPushButton:hover{\n"
        #                                 "   background-color:rgb(84, 42, 255);\n"
        #                                 "}")
        #
        #
        # layout.addWidget(button)



    def sizeHint(self):
        # 决定item的高度
        return QSize(200, 40)


class SortFilterProxyModel(QSortFilterProxyModel):

    def lessThan(self, source_left, source_right):
        if not source_left.isValid() or not source_right.isValid():
            return False
        # 获取数据
        leftData = self.sourceModel().data(source_left)
        rightData = self.sourceModel().data(source_right)
        if self.sortOrder() == Qt.DescendingOrder:
            # 按照时间倒序排序
            leftData = leftData.split('-')[-1]
            rightData = rightData.split('-')[-1]
            return leftData < rightData
        #         elif self.sortOrder() == Qt.AscendingOrder:
        #             #按照名字升序排序
        #             leftData = leftData.split('-')[0]
        #             rightData = rightData.split('-')[0]
        #             return leftData < rightData
        return super(SortFilterProxyModel, self).lessThan(source_left, source_right)


class mail_list(QWidget):
    look_signal = QtCore.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(mail_list, self).__init__(*args, **kwargs)

        self.resize(701, 500)
        self.setMinimumSize(QtCore.QSize(682, 466))
        layout = QVBoxLayout(self)
        self.layout().setContentsMargins(0,0,0,0)
        # 名字排序
        # listview
        self.listView = QListView(self)
        self.listView.doubleClicked.connect(self.look_signal)
        layout.addWidget(self.listView)
        # 数据模型
        self.dmodel = QStandardItemModel(self.listView)
        self.listView.currentIndex()


        # 排序代理模型
        self.fmodel = SortFilterProxyModel(self.listView)
        self.fmodel.setSourceModel(self.dmodel)
        self.listView.setModel(self.fmodel)

    def show_mail(self, mail):
        if len(mail) == 0:
            pass
        else:
            for num, content in mail.items():
                sender = content["from"][1]
                subject = content["subject"]
                text = "发送者: " + sender + "   主题: " + subject
                item = QStandardItem(text)
                #             item.setData(value, Qt.UserRole + 2)
                self.dmodel.appendRow(item)
                index = self.fmodel.mapFromSource(item.index())
                # 自定义的widget
                widget = CustomWidget(text, self)
                item.setSizeHint(widget.sizeHint())
                self.listView.setIndexWidget(index, widget)





if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = mail_list()
    w.show()
    sys.exit(app.exec_())