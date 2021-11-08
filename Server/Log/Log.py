"""
-*- coding: utf-8 -*-
@Time    : 2021/11/8 23:25
@Author  : 夕照深雨
@File    : Log.py
@Software: PyCharm

Attention：

"""
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
        handler = RotatingFileHandler("Log/" + desk + '.log', 'a', 5024 * 1024, 1000000, 'utf8')
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
