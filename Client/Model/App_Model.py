"""
-*- coding: utf-8 -*-
@Time    : 2022/1/2 16:33
@Author  : 夕照深雨
@File    : App_Model.py
@Software: PyCharm

Attention：

"""
import base64
import json
import random
import sys
import socket, sys
from imaplib import Int2AP

HOST = "127.0.0.1"
PORT = 53831  # 端口号
_GLOBAL_DEFAULT_TIMEOUT = object()  # 超时参数
CRLF = b'\r\n'


class App_Model:
    """
    和服务端建立网络连接
    """

    class error(Exception):
        pass  # Logical errors - debug required

    class abort(error):
        pass  # Service errors - close and retry

    def __init__(self, host=HOST, port=PORT, timeout=None):
        self.data = b""
        self.host = host
        self.port = port
        self.sock = None

    def open(self, host=HOST, port=PORT, timeout=None):
        """
        打开socket链接
        Args:
            host: 主机
            port: 地址
            timeout: 超时

        Returns:

        """
        self.sock = self._create_socket(timeout)

    def _create_socket(self, timeout):
        """
        判断是否超时，建立socket连接
        Args:
            timeout: 超时

        Returns:

        """
        if timeout is not None and not timeout:
            raise ValueError('Non-blocking socket (timeout=0) is not supported')
        host = None if not self.host else self.host
        sys.audit("App_Connection.open", self, self.host, self.port)
        address = (host, self.port)
        if timeout is not None:
            return socket.create_connection(address, timeout)
        return socket.create_connection(address)

    def send_rec_msg(self, message: bytes):
        """
        发送和接受信息
        Args:
            message: 传入

        Returns:

        """
        message = bytes(json.dumps(message), encoding="utf8")
        self.open(self.host, self.port)  # 打开链接
        self.sock.sendall(message+CRLF)  # 发送信息
        self.data = b""
        temp_data = self.sock.recv(1024)
        self.data += temp_data
        while len(temp_data) == 1024:  # 用于接收分段文件并合并
            temp_data = self.sock.recv(1024)
            self.data += temp_data
            if temp_data[-2:] == CRLF:  # 遇到停止符号结束接收
                break

        self.data = json.loads(self.data[:-2].decode())  # 接收客户端信息
        self.sock.close()  # 关闭连接
        return self.data

    def register(self, username, password):
        """
        注册新账号
        命令格式：
        {"action": "register",
                   "content": {
                       "username": username,
                       "password": password
                    }
                }
        Args:
            username: 用户名
            password: 密码

        Returns:

        """
        message = {"action": "register",
         "content": {
             "username": username,
             "password": password
         }
         }
        rec = self.send_rec_msg(message)
        return rec

    def add_account(self, username, password, account):
        """
        添加邮箱
        命令格式：
        {"action": "add_account",
                   "content": {
                       "username": username,
                       "password": password,
                       "account": account
                    }
                }
        Args:
            username: 用户名
            password: 密码

        Returns:

        """
        message = {"action": "add_account",
         "content": {
             "username": username,
             "password": password,
             "account": account
         }
         }
        rec = self.send_rec_msg(message)
        return rec



    def send_email(self, sender, receiver, sender_name, content, title, attachment = None):
        """
        发送电子邮件
        发送的命令格式：
        {
                "action" : "send_email",
                "content": {
                  "sender" : sender,
                  "sender_name": sender_name,
                  "receiver" : receiver,
                  "subject": subject,
                  "text": text,
                  "attachment": attachment
                }
        }
        Args:
            attachment: 字典： 附件名，附件的路径
            sender: 发送者
            receiver: 接受者
            sender_name: 用户名
            content: 内容
            title: 主题


        Returns:

        """
        message = {
                "action" : "send_email",
                "content": {
                  "sender" : sender,
                  "sender_name": sender_name,
                  "receiver" : receiver,
                  "subject": title,
                  "text": content,
                  "attachment": None
                }
        }
        if attachment is not None:  # 将附件放入消息中
            message["content"]["attachment"] = {}
            for filename,filepath in attachment.items():
                with open(filepath, 'rb') as f:
                    file_byte = base64.b64encode(f.read())
                file_str = file_byte.decode("ascii")
                message["content"]["attachment"][filename] = file_str

        rec = self.send_rec_msg(message)
        return rec

    def login(self, username, password):
        """
        向服务器发送登陆命令
        命令格式：
        {"action": "login",
                   "content": {
                       "username": username,
                       "password": password
                    }
                }
        Args:
            username: 用户名
            password: 密码

        Returns:
            验证结果

        """

        message = {"action": "login",
                   "content": {
                       "username": username,
                       "password": password
                   }
                   }
        # 命令格式

        rec = self.send_rec_msg(message)
        return rec


if __name__ == "__main__":
    App = App_Model()
    App.listen()
