"""
-*- coding: utf-8 -*-
@Time    : 2022/1/4 0:48
@Author  : 夕照深雨
@File    : Message_handler.py
@Software: PyCharm

Attention：

"""
import base64
import logging

from Server.Application.Send_Mail import SendMail
from Server.DAO.DAO_email_account import DAO_email_account
from Server.DAO.DAO_file_email import DAO_file_email
from Server.DAO.DAO_transaction_records import DAO_transaction_records
from Server.Log.Log import Logger
from Server.DAO.DAO_email_user import DAO_email_user
from Server.Utils.Snowflake import IdWorker

logger = Logger("../Log/server_history.log", logging.DEBUG, __name__).getlog()
Attachment_path = "../Attachment/"


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
        return message

    def send_email(self):
        """
        发送邮件到指定邮箱
        接受的命令格式：
        {
                "action" : "send_email",
                "content": {
                  "sender" : sender,
                  "sender_name": sender_name,
                  "receiver" : receiver,
                  "subject": subject,
                  "text": text,
                  ”attachment“ : attachment
                }
        }
        Returns:

        """
        sender = self.message["content"]["sender"]
        sender_name = self.message["content"]["sender_name"]
        receiver = self.message["content"]["receiver"]
        subject = self.message["content"]["subject"]
        text = self.message["content"]["text"]
        attachment = self.message["content"]["attachment"]

        database1 = DAO_email_account()
        database2 = DAO_file_email()
        database3 = DAO_transaction_records()

        password = database1.select_password(sender)  # 查询用户密码
        if password is None:
            message = {
                "action": "send_mail_response",
                "content": {
                    "status": "False",
                    "reason": "发送失败"
                }
            }
        else:
            email_id = IdWorker(15).get_id()
            database3.insert(email_id, sender, receiver, text, subject)  # 插入发送记录

            file_list = []

            if attachment is not None:  # 将附件重命名存入服务器本地
                for filename, file_str in attachment.items():
                    file_id = IdWorker(15).get_id()
                    file_list.append(file_id)
                    file_byte = base64.b64decode(file_str)
                    file_json = open(Attachment_path + file_id, 'wb')
                    file_json.write(file_byte)
                    file_json.close()
                    database2.insert(email_id, file_id, filename)  # 插入邮件和附件的对应关系

            mail = SendMail(receiver, sender_name, subject, text, sender, password, file_list)
            res = mail.send_email()  # 发送邮件

            if res:
                message = {
                    "action": "send_mail_response",
                    "content": {
                        "status": "True",
                        "reason": "发送成功"
                    }
                }
            else:
                message = {
                    "action": "send_mail_response",
                    "content": {
                        "status": "False",
                        "reason": "发送失败"
                    }
                }
        return message

    def login(self):
        """
        验证账号密码
        接受的命令格式：
        {
        "action": "login",
                   "content": {
                       "username": username,
                       "password": password
                    }
                   }
        Returns:
            None 账号不存在
            True 账号密码正确
            False 密码错误

        """
        username = self.message["content"]["username"]
        password = self.message["content"]["password"]
        database = DAO_email_user()
        res = database.login_user(username, password)

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
