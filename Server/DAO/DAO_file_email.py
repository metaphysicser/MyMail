"""
-*- coding: utf-8 -*-
@Time    : 2022/1/7 23:32
@Author  : 夕照深雨
@File    : DAO_file_email.py
@Software: PyCharm

Attention：

"""
from Server.DAO.DAO_base import DAO_base
from Server.Log.Log import Logger
import logging


logger = Logger("../Log/database.log", logging.DEBUG, __name__).getlog()


class DAO_file_email(DAO_base):
    """
    连接数据库中的email_file表，并执行相关操作

    """
    def insert(self, email_id: str, file_id: str, file_name: str):
        """
        插入附件邮件对应关系记录
        Args:
            file_name: 附件名
            file_id: 附件UID
            email_id: 邮件UID
        """


        sql = """INSERT INTO file_email(email_id,
                 file_id, file_name)
                 VALUES (%s, %s, %s)"""
        if self.execute(sql,email_id, file_id, file_name) != False:
            logger.info("transaction_records表 插入{}, {}记录成功".format(email_id, file_id))
        else:
            logger.info("transaction_records表 插入{}, {}记录失败".format(email_id, file_id))

if __name__ == "__main__":
    d = DAO_file_email()
    d.insert("12","13", "13")
