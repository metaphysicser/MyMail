"""
-*- coding: utf-8 -*-
@Time    : 2021/11/9 0:21
@Author  : 夕照深雨
@File    : DAO_base.py
@Software: PyCharm

Attention：

"""
import logging
import os

import pymysql
import configparser
from Server.Log.Log import Logger

logger = Logger("../Log/database.log", logging.DEBUG, __name__).getlog()

CONFIG_PATH = "../DAO/config.ini"


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

    def execute(self, sql_query: str,*kwargs):
        """
        执行sql查询语句
        Args:
            sql_query: sql查询语句
            *kwargs: 值参数

        Returns:查询结果

        """

        try:
            self.cursor.execute(sql_query,kwargs)
            self.conn.commit()
            return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            logger.error(e)
            return False

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.conn.close()
