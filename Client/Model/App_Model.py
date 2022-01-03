"""
-*- coding: utf-8 -*-
@Time    : 2022/1/2 16:33
@Author  : 夕照深雨
@File    : App_Model.py
@Software: PyCharm

Attention：

"""
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
        self.open(self.host, self.port)  # 打开链接
        self.sock.send(message)   # 发送信息
        self.data = b""
        while self.data == b"":
            self.data = self.sock.recv(1024)  # 接收信息
        self.data = json.loads(self.data.decode())
        self.sock.close()  # 关闭连接
        return self.data

    def login(self, username, password):
        """
        向服务器发送登陆命令
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
        message = bytes(json.dumps(message), encoding = "utf8")
        rec = self.send_rec_msg(message)
        return rec


if __name__ == "__main__":
    App = App_Model()
    App.listen()
