"""
-*- coding: utf-8 -*-
@Time    : 2021/11/8 23:33
@Author  : 夕照深雨
@File    : DAO_mailserver.py
@Software: PyCharm

Attention：

"""
import pymysql
from Server.Log.Log import get_logger
from DAO_base import DAO_base

logger = get_logger("../Log/db_history")

class DAO_email_user(DAO_base):
    """
    连接数据库中的email_user表，并执行相关操作

    """
    def execute(self, sql_query: str):
        """
        执行sqlc查询语句
        
        :param sql_query: 
        :return: 
        """
        try:
            self.conn.execute(sql_query)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.error(e)
        self.close()

    def insert(self, email: str, password: str, salt_scrypt: str, salt_bcrypt: str):
        """
        插入数据

        :param email: 邮箱
        :param password: 密码
        :param salt_scrypt: 盐
        :param salt_bcrypt: 盐
        :return:
        """

        sql = """INSERT INTO email_user(email,
                 password, salt_scrypt, salt_bcrypt)
                 VALUES ('%s', '%s', '%s', '%s')""" % (email, password, salt_scrypt, salt_bcrypt)
        self.execute(sql)





d = DAO_email_user()
d.insert("zpl010720@qq.com", "password", "twatgeawg", "fwqtwtg")

