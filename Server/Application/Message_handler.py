"""
-*- coding: utf-8 -*-
@Time    : 2022/1/4 0:48
@Author  : 夕照深雨
@File    : Message_handler.py
@Software: PyCharm

Attention：

"""
import logging
from Server.Log.Log import Logger
from Server.DAO.DAO_email_user import DAO_email_user

logger = Logger("../Log/server_history.log", logging.DEBUG, __name__).getlog()


class Message_handler:
    """
    处理不同的信息，给出不同的回应
    """

    def __init__(self):
        self.message = None

    def handle(self, message):
        """
        处理消息
        Args:
            message: 消息

        Returns: 处理结果

        """
        self.message = message
        print(message)
        action = self.message["action"]  # 类型
        res = self.command(action)  # 根据消息类型调用不同的函数
        return res

    def command(self, action):
        """
        调用不同函数
        Args:
            action: 类型

        Returns:

        """
        message = getattr(self, action, self.undefined)()  # 调用对应的函数，否则调用undefined
        print(message)
        return message

    def login(self):
        """
        验证账号密码
        Returns:

        """
        username = self.message["content"]["username"]
        password = self.message["content"]["password"]
        database = DAO_email_user()
        res = database.login_user(username, password)
        print(res)

        if res is None:  # 账号不存在
            message = {"action": "login_response",
                       "content": {
                           "status": "False",
                           "reason": "账号不存在"
                       }
                       }
        elif res:  # 密码正确
            message = {"action": "login_response",
                       "content": {
                           "status": "True",
                           "reason": "登陆成功"
                       }
                       }
        else:  # 密码错误
            message = {"action": "login_response",
                       "content": {
                           "status": "False",
                           "reason": "密码不正确"
                       }
                       }
        return message

    def undefined(self):
        pass
