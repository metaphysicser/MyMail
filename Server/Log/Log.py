"""
-*- coding: utf-8 -*-
@Time    : 2021/11/8 23:25
@Author  : 夕照深雨
@File    : Log.py
@Software: PyCharm

Attention：

"""
import logging


# 既把日志输出到控制台， 还要写入日志文件
class Logger():
    def __init__(self, logname="info", loglevel=logging.DEBUG, loggername=None):
        """
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        """
        # 创建一个logger
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(loglevel)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname,encoding="utf8")
        fh.setLevel(loglevel)
        if not self.logger.handlers:
            # 再创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(loglevel)
            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

