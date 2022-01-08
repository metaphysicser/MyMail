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
    def insert(self, email_id: str, sender: str, receiver: str, content: str, title:str):
        """
        插入邮件发送记录
        Args:
            content: 邮件内容
            title: 主题
            receiver: 接受者
            sender: 发送者
            email_id: 邮件UID
        """

        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        sql = """INSERT INTO transaction_records(email_id,
                 sender, receiver, content, time, title)
                 VALUES (%s, %s, %s,%s,%s,%s)"""
        if self.execute(sql,email_id, sender,receiver, content, now, title) != False:
            logger.info("transaction_records表 插入{}, {}, {}, {} ,{}, {} 记录成功".format(email_id, sender,receiver, content, now, title))
        else:
            logger.info("transaction_records表 插入{}, {}, {}, {}, {}, {} 记录失败".format(email_id, sender,receiver, content, now, title))

if __name__ == "__main__":
    d = DAO_transaction_records()
    d.insert("12","zpl01020@qq.com", "fewa@ee.com", "test","test")
