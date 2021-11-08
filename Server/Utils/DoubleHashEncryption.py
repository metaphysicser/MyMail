"""
-*- coding: utf-8 -*-
@Time    : 2021/11/8 17:14
@Author  : 夕照深雨
@File    : DoubleHashEncryption.py
@Software: PyCharm

Attention：

"""
import bcrypt
import scrypt
import os


def verify_password_bcrypt(password, hashed_password):
    if bcrypt.checkpw(password, hashed_password):
        return True
    else:
        return False

def verify_password_scrypt(hashed_password, guessed_password, max_time=0.5):
    try:
        scrypt.decrypt(hashed_password, guessed_password, max_time)
        return True
    except scrypt.error:
        return False

def hash_password_scrypt(password: bytes, salt: bytes):
    """
    对密码进行scrypt哈希

    :param password: 密码，字节
    :param salt: 盐，字节
    :return: 加密后的密码
    """
    return scrypt.hash(password, salt)


def hash_password_bcrypt(password: str, salt: bytes):
    """
    对密码进行crypt哈希

    :param password: 密码，字符
    :param salt: 盐，字节
    :return: 加密后的密码
    """
    return bcrypt.hashpw(password.encode(), salt)


class DoubleHashEncryption(object):
    """
    加盐的双重慢哈希加密

    使用 bcrypt 和 scrypt 算法进行密码加密，提高计算复杂度，有效防止暴力破解和查表法
    """

    def __init__(self, data_length=64):
        """

        :param data_length: scrypt 算法的数据长度
        """
        self.data_length = data_length
        self.salt_scrypt = os.urandom(self.data_length) # scrypt的盐
        self.salt_bcrypt = bcrypt.gensalt()  # bcrypt的盐


    def get_salt_bcrypt(self):
        """
        获取bcrypt的盐

        :return: bcrypt的盐
        """
        return self.salt_bcrypt

    def get_salt_scrypt(self):
        """
        获取scrypt的盐
        :return:
        """
        return self.salt_scrypt

    def double_hash_encryption(self, password: str) -> bytes:
        """
        双重哈希加密

        :param password: 密码，字符串
        :return: 加密密码， 字节流
        """
        return hash_password_bcrypt(str(hash_password_scrypt(password, self.salt_scrypt)), self.salt_bcrypt)

    def verify_double_hash(self, password: str, hash_password: bytes, salt_scrypt: bytes, salt_bcrypt: bytes):
        """
        验证密码正确性

        :param password: 密码
        :param hash_password: 加密后密码
        :param salt_scrypt: scrypt的盐
        :param salt_bcrypt: bcypt的盐
        :return: 是否正确
        """

        if hash_password == self.double_hash_encrption(password, salt_scrypt, salt_bcrypt):
            return True
        else:
            return False

