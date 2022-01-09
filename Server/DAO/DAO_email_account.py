"""
-*- coding: utf-8 -*-
@Time    : 2022/1/8 2:07
@Author  : 夕照深雨
@File    : DAO_email_account.py
@Software: PyCharm

Attention：

"""
from Server.DAO.DAO_base import DAO_base
from Server.Log.Log import Logger
from Server.Utils.RSA_encryption import RSA_encryption
import logging

from Server.Utils.DoubleHashEncryption import DoubleHashEncryption

logger = Logger("../Log/database.log", logging.DEBUG, __name__).getlog()


class DAO_email_account(DAO_base):
    """
    连接数据库中的email_account表，并执行相关操作

    """

    def insert(self, account: str, user_name: str, password: str):
        """
        插入附件邮件对应关系记录
        Args:
            password: 密码
            user_name: 用户名
            account: 邮箱

        """
        r = RSA_encryption()
        password = r.encrypt_data(password)
        private_key = r.get_private_key()

        sql = """INSERT INTO email_account(account, user_name,password,private_key)
                        VALUES (%s, %s, %s, %s)"""

        result = self.execute(sql, account, user_name, password, private_key)

        if result != False:
            logger.info(
                "email_user表 插入{}, {}, {}, {} 记录成功".format(account, user_name, password, private_key))
            return True
        else:
            logger.info(
                "email_user表 插入{}, {}, {}, {} 记录失败".format(account, user_name, password, private_key))
            return False

    def select_password(self, account: str) -> bool:
        """
        获取邮箱账号密码
        Args:
            account: 邮箱账号

        Returns:密码

        """
        sql = """select password, private_key from email_account where account = %s"""
        result = self.execute(sql, account)
        if result != False and len(result) != 0:
            password, private_key = result[0]
            r = RSA_encryption()
            password = r.decrypt_data(password, private_key)
            return password
        else:
            return None

    def select_account(self, username: str) -> bool:
        """
        获取用户关联邮箱账号
        Args:
            username: 用户名

        Returns:密码

        """
        sql = """select account from email_account where user_name = %s"""
        result = self.execute(sql, username)
        if result != False and len(result) != 0:
            account = result[0]
            return account
        else:
            return None


if __name__ == "__main__":
    d = DAO_email_account()
    d.insert("zpl010720@qq.com","124","esnkoqfbkduucejh")
