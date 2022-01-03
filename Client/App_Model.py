"""
-*- coding: utf-8 -*-
@Time    : 2022/1/2 16:33
@Author  : 夕照深雨
@File    : App_Model.py
@Software: PyCharm

Attention：

"""
import sys
import socket, sys

PORT = 53831  # 端口号
_GLOBAL_DEFAULT_TIMEOUT = object() # 超时参数


class App_Model:
    """
    和服务端建立网络连接
    """

    class error(Exception):
        pass  # Logical errors - debug required

    class abort(error):
        pass  # Service errors - close and retry

    def __init__(self, host='', port=PORT, timeout=None):
        self.state = 'LOGOUT'
        self.data = b""
        self.open(host, port, timeout)


    def open(self, host='', port=PORT, timeout=None):
        """
        打开sockect链接
        Args:
            host: 主机
            port: 地址
            timeout: 超时

        Returns:

        """
        self.host = host
        self.port = port
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

    def listen(self):
        while(True):
            self.data = b""
            while True:
                self.data += self.request.recv(1024)
                if self.data.endswith(b"\r\n"):
                    self.data = self.data[0:-2].decode()
                    break

if __name__ == "__main__":
    App = App_Model()
    App.listen()


