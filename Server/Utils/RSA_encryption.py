"""
-*- coding: utf-8 -*-
@Time    : 2022/1/8 18:50
@Author  : 夕照深雨
@File    : RSA_encryption.py
@Software: PyCharm

Attention：

"""
from Crypto import Random
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)


class RSA_encryption:
    """
    使用RSA非对称算法进行加密
    """
    def __init__(self):
        self.private_key = rsa.exportKey()
        self.public_key = rsa.publickey().exportKey()

    def encrypt_data(self, password):
        """
        加密
        Args:
            password: 密码

        Returns:
            加密后的密码

        """
        public_key = RSA.importKey(self.public_key)
        cipher = PKCS1_cipher.new(public_key)
        encrypt_text = base64.b64encode(cipher.encrypt(bytes(password.encode("utf8"))))
        return encrypt_text.decode('utf-8')

    def decrypt_data(self, encrypt_msg, private_key):
        """
        解密密码
        Args:
            encrypt_msg: 加密后的密码
            private_key: 私钥

        Returns:
            解密后的密码

        """
        private_key = RSA.importKey(private_key)
        cipher = PKCS1_cipher.new(private_key)
        back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)
        return back_text.decode('utf-8')

    def get_private_key(self):
        """
        获得私钥
        Returns:

        """
        return self.private_key
