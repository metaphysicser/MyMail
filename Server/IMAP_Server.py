"""
-*- coding: utf-8 -*-
@Time    : 2021/11/4 10:40
@Author  : 夕照深雨
@File    : IMAP_Server.py
@Software: PyCharm

Attention：

"""
import socket
import threading
import socketserver
import time
from logging.config import dictConfig
import logging
from logging.handlers import RotatingFileHandler

from IMAPLib import IMAP

logger_map = {

}

# 获取指定房间的日志记录器
def get_logger(desk):
    if desk not in logger_map.keys():
        # 获取日志记录器
        logger = logging.getLogger(desk)
        logger.setLevel(logging.INFO)

        # 滚动日志处理器
        handler = RotatingFileHandler(desk + '.log', 'a', 5024 * 1024, 1000000, 'utf8')
        handler.setLevel(logging.INFO)

        # 创建一个格式器formatter并将其添加到处理器handler
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')
        handler.setFormatter(formatter)

        # 为日志器logger添加上面创建的处理器handler
        logger.addHandler(handler)
        logger_map[desk] = logger
    return logger_map[desk]
logger = get_logger("history")

CRLF = b'\r\n'

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):#继承ThreadingMixIn表示使用多线程处理request
    pass

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self): # 重写handle方法
        cur_thread = threading.current_thread()
        imap = IMAP()
        try:
            while True:
                self.data = self.request.recv(1024)

                if self.data.endswith(b"\r\n"):
                    self.data = self.data[:-2]
                self.data = self.data.decode()

                logger.info("ip {} 向服务器线程 {} 发送信息:".format(self.client_address[0], cur_thread.name)+self.data)
                # if not self.data:
                #     logger.error("ip {} 和服务器线程 {} 链接丢失".format(self.client_address[0], cur_thread.name))
                #     break

                res = imap.handle_command(self.data)
                for message in res:
                    self.request.sendall(message.encode()+CRLF)
        except Exception as e:
            logger.error("ip {} 和服务器线程 {} 链接断开".format(self.client_address[0], cur_thread.name))
            print(e)
        finally:
            self.request.close()

    def setup(self): # handle方法之前调用
        cur_thread = threading.current_thread()
        logger.info("服务器线程{}开启".format(cur_thread.name))
        self.request.send("* OK IMAP4rev1 server ready".encode()+CRLF)
        logger.info("ip {} 向服务器线程 {} 发送信息:".format(self.client_address[0], cur_thread.name) + "* OK IMAP4rev1 server ready")



    def finish(self): # handle方法之后调用
        cur_thread = threading.current_thread()
        logger.info("服务器线程{}关闭".format(cur_thread.name))




if __name__ == "__main__":
    HOST, PORT = "localhost", 143

    # 实例化对象，绑定本地端口143
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    # server_thread.daemon = True
    logger.info("IMAP服务器开始工作，监听端口{}".format(str(port)))
    server_thread.start()

    # server.shutdown()



