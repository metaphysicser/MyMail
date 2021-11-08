"""
-*- coding: utf-8 -*-
@Time    : 2021/11/4 10:40
@Author  : 夕照深雨
@File    : IMAP_Server.py
@Software: PyCharm

Attention：

"""

import threading
import socketserver
from typing import Any
from IMAPLib import IMAP
import logging
from logging.handlers import RotatingFileHandler

logger_map = {

}


# 获取指定房间的日志记录器
def get_logger(desk):
    if desk not in logger_map.keys():
        # 获取日志记录器
        logger_ = logging.getLogger(desk)
        logger_.setLevel(logging.INFO)

        # 滚动日志处理器
        handler = RotatingFileHandler(desk + '.log', 'a', 5024 * 1024, 1000000, 'utf8')
        handler.setLevel(logging.INFO)

        # 创建一个格式器formatter并将其添加到处理器handler
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')
        handler.setFormatter(formatter)

        # 为日志器logger添加上面创建的处理器handler
        logger_.addHandler(handler)
        logger_map[desk] = logger_
    return logger_map[desk]


logger = get_logger("history")

CRLF = b'\r\n'


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):  # 继承ThreadingMixIn表示使用多线程处理request
    pass


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request: Any, client_address: Any, server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.data = b""

    def handle(self):  # 重写handle方法
        cur_thread = threading.current_thread()
        imap = IMAP()

        try:
            while True:
                self.data = b""
                while True:
                    self.data += self.request.recv(1024)
                    if self.data.endswith(b"\r\n"):
                        self.data = self.data[0:-2].decode()
                        break

                logger.info("ip {} 向服务器线程 {} 发送信息:".format(self.client_address[0], cur_thread.name) + self.data)
                # if not self.data:
                #     logger.error("ip {} 和服务器线程 {} 链接丢失".format(self.client_address[0], cur_thread.name))
                #     break

                res = imap.handle_command(self.data)
                for message in res:
                    self.request.sendall(message.encode() + CRLF)
                    logger.info("服务器线程 {} 向 ip {} 发送信息:".format(cur_thread.name, self.client_address[0]) + message)
        except Exception as e:
            logger.error("ip {} 和服务器线程 {} 链接断开".format(self.client_address[0], cur_thread.name))
            logger.error(e)
        finally:
            self.request.close()

    def setup(self):  # handle方法之前调用
        cur_thread = threading.current_thread()
        logger.info("服务器线程{}开启".format(cur_thread.name))
        self.request.send("* OK IMAP4rev1 server ready".encode() + CRLF)
        logger.info(
            "ip {} 向服务器线程 {} 发送信息:".format(self.client_address[0], cur_thread.name) + "* OK IMAP4rev1 server ready")

    def finish(self):  # handle方法之后调用
        cur_thread = threading.current_thread()
        logger.info("服务器线程{}关闭".format(cur_thread.name))


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 143

    # 实例化对象，绑定本地端口143
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    # server_thread.daemon = True
    logger.info("IMAP服务器开始工作，监听端口{}".format(str(port)))
    server_thread.start()

    # server.shutdown()
