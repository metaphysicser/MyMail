"""
-*- coding: utf-8 -*-
@Time    : 2021/12/31 22:33
@Author  : 夕照深雨
@File    : Application_Server.py
@Software: PyCharm

Attention：

"""
import json
import threading
import socketserver
from typing import Any
import logging
from Server.Log.Log import Logger
from Server.Application.Message_handler import Message_handler

CRLF = b'\r\n'
Buffer = 1024  # 接收缓冲区长度

logger = Logger("../Log/AppServer_history.log", logging.DEBUG, __name__).getlog()


class ThreadedAPPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):  # 继承ThreadingMixIn表示使用多线程处理request
    pass


class ThreadedAPPRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request: Any, client_address: Any, server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.data = b""

    def handle(self):  # 重写handle方法
        cur_thread = threading.current_thread()
        handler = Message_handler()

        try:
            while True:
                self.data = b""
                temp_data = self.request.recv(Buffer)
                self.data += temp_data
                while len(temp_data) == Buffer:  # 用于接收分段文件并合并
                    temp_data = self.request.recv(Buffer)
                    self.data += temp_data
                    if temp_data[-2:] == CRLF:  # 遇到停止符号结束接收
                        break

                self.data = str(self.data[:-2], 'utf8').replace("'", '"')
                self.data = json.loads(self.data)  # 接收客户端信息

                logger.info("ip {} 向APP服务器线程 {} 发送信息:".format(self.client_address[0], cur_thread.name) + str(self.data))
                if not self.data:
                    logger.error("ip {} 和APP服务器线程 {} 链接丢失".format(self.client_address[0], cur_thread.name))
                    break

                message = handler.handle(self.data)  # 处理客户端信息
                message_bit = bytes(json.dumps(message), encoding="utf8") + CRLF
                self.request.send(message_bit)

                logger.info("服务器APP线程 {} 向 ip {} 发送信息:".format(cur_thread.name, self.client_address[0]) + str(message))
        except Exception as e:
            logger.error("ip {} 和APP服务器线程 {} 链接断开".format(self.client_address[0], cur_thread.name))
            logger.error(e)
        finally:
            self.request.close()

    def setup(self):  # handle方法之前调用
        cur_thread = threading.current_thread()
        logger.info("服务器线程{}开启".format(cur_thread.name))

    def finish(self):  # handle方法之后调用
        cur_thread = threading.current_thread()
        logger.info("APP服务器线程{}关闭".format(cur_thread.name))


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 53831

    # 实例化对象，绑定本地端口143
    server = ThreadedAPPServer((HOST, PORT), ThreadedAPPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    # server_thread.daemon = True
    logger.info("APP服务器开始工作，监听端口{}".format(str(port)))
    server_thread.start()

    # server.shutdown()
