"""
-*- coding: utf-8 -*-
@Time    : 2021/11/8 23:33
@Author  : 夕照深雨
@File    : DAO_mailserver.py
@Software: PyCharm

Attention：

"""
import logging

import pymysql
from Server.Log.Log import Logger
from DAO_base import DAO_base

logger = Logger("../Log/database.log", logging.DEBUG, __name__).getlog()

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
            self.cursor.execute(sql_query)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            logger.error(e)
            return False


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
        if self.execute(sql):
            logger.info("mailserver表 插入{}, {}, {}, {} 记录成功".format(email, password, salt_scrypt, salt_bcrypt))
        else:
            logger.info("mailserver表 插入{}, {}, {}, {} 记录失败".format(email, password, salt_scrypt, salt_bcrypt))




d = DAO_email_user()
d.insert("zpl01020@qq.com", "password", "twatgeawg", "fwqtwtg")

