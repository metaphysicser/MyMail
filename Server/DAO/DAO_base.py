"""
-*- coding: utf-8 -*-
@Time    : 2021/11/9 0:21
@Author  : 夕照深雨
@File    : DAO_base.py
@Software: PyCharm

Attention：

"""
import pymysql
import configparser
from Server.Log.Log import get_logger

logger = get_logger("../Log/db_history")

CONFIG_PATH = "config.ini"


class DAO_base():
    """
    数据库访问的基类

    """

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        self.host = config['DATABASE']['host']
        self.port = int(config['DATABASE']['port'])
        self.user = config['DATABASE']['user']
        self.password = config['DATABASE']['password']
        self.charset = config['DATABASE']['charset']
        self.db = config['DATABASE']['db']
        self.conn = self.get_conn()
        self.cursor = self.conn.cursor()

    def get_conn(self):
        """
        打开数据库连接
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                   database=self.db, charset=self.charset)
            return conn
        except Exception as e:
            logger.error(e)

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.conn.close()
