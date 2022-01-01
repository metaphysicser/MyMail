"""
-*- coding: utf-8 -*-
@Time    : 2022/1/2 1:40
@Author  : 夕照深雨
@File    : DAO_email_user.py
@Software: PyCharm

Attention：

"""

from Server.DAO.DAO_base import DAO_base
from Server.Log.Log import Logger
import logging
from Server.Utils.DoubleHashEncryption import DoubleHashEncryption
logger = Logger("../Log/database.log", logging.DEBUG, __name__).getlog()


class DAO_email_user(DAO_base):
    """
    连接数据库中的email_user表，并执行相关操作

    """
    def register_user(self, username: str, password: str)->bool:
        """
        注册新的账号

        :param username: 用户名
        :param password: 密码
        :return: 是否注册成功
        """

        dhe = DoubleHashEncryption() # 双重hash加密
        salt_scrypt = dhe.get_salt_scrypt()
        salt_bcrypt = dhe.get_salt_bcrypt()
        password = dhe.double_hash_encryption(password)


        sql = """INSERT INTO email_user(username,password,salt_scrypt,salt_bcrypt)
                 VALUES (%s, %s, %s,%s)"""


        if self.execute(sql,username,password,salt_scrypt,salt_bcrypt):
            logger.info("email_user表 插入{}, {}, {}, {} 记录成功".format(username, password, salt_scrypt, salt_bcrypt))
        else:
            logger.info("email_user表 插入{}, {}, {}, {} 记录失败".format(username, password, salt_scrypt, salt_bcrypt))

if __name__ == "__main__":
    d = DAO_email_user()
    d.register_user("124","125")