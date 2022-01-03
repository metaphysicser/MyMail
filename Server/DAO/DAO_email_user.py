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

        result = self.execute(sql, username,password,salt_scrypt,salt_bcrypt)

        if result != False:
            logger.info("email_user表 插入{}, {}, {}, {} 记录成功".format(username, password, salt_scrypt, salt_bcrypt))
            return True
        else:
            logger.info("email_user表 插入{}, {}, {}, {} 记录失败".format(username, password, salt_scrypt, salt_bcrypt))
            return False

    def login_user(self, username:str, password: str)->bool:
        """
        验证账号密码的正确性
        Args:
            account: 账号
            password: 密码

        Returns:密码是否正确

        """
        sql = """select password, salt_scrypt, salt_bcrypt from email_user where username = %s"""

        result = self.execute(sql,username)

        print(result)

        if len(result) != 0: # 是否存在该账号
            password_db, salt_scrypt, salt_bcrypt = result[0]
            dbe = DoubleHashEncryption()
            if dbe.verify_double_hash(password, password_db, salt_scrypt, salt_bcrypt):
                logger.info("系统查询email_user表的用户{}, 输入密码为{}, 注册密码为{}，一致允许登陆".format(username, password,password_db))
                return True
            else:
                logger.info("系统查询email_user表的用户{}, 输入密码为{}, 注册密码为{}，不一致不允许登陆".format(username, password, password_db))
                return False
        else:
            logger.info("系统查询email_user表的用户{}不存在".format(username))
            return None

    def delete_user(self,username)->bool:
        """
        删除账户
        Args:
            username: 用户名

        Returns: 删除是否成功

        """
        sql = """delete from email_user where username = %s """

        result = self.execute(sql, username)

        if result != False:
            logger.info("系统删除email_user表的用户{}成功".format(username))
            return True
        else:
            logger.info("系统删除email_user表的用户{}失败".format(username))
            return False




if __name__ == "__main__":
    d = DAO_email_user()
    d.register_user("124","125")
    d.delete_user("124")