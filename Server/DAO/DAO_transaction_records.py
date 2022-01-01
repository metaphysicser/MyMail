"""
-*- coding: utf-8 -*-
@Time    : 2021/11/9 19:20
@Author  : 夕照深雨
@File    : DAO_transaction_records.py
@Software: PyCharm

Attention：

"""

from Server.DAO.DAO_base import DAO_base
from Server.Log.Log import Logger
import logging
import time

logger = Logger("../Log/database.log", logging.DEBUG, __name__).getlog()


class DAO_transaction_records(DAO_base):
    """
    连接数据库中的transaction_records表，并执行相关操作

    """
    def insert(self, source: str, target: str, content: str):
        """
        插入数据

        :param target: 目标邮箱
        :param source: 来源邮箱
        :param content: 邮件内容
        :return:
        """

        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        sql = """INSERT INTO transaction_records(source,
                 target, content, time)
                 VALUES ('%s', '%s', '%s','%s')"""
        if self.execute(sql,source, target, content, now):
            logger.info("transaction_records表 插入{}, {}, {}, {} 记录成功".format(source, target, content, now))
        else:
            logger.info("transaction_records表 插入{}, {}, {}, {} 记录失败".format(source, target, content, now))

if __name__ == "__main__":
    d = DAO_transaction_records()
    d.insert("zpl01020@qq.com", "fewa@ee.com", "test")
