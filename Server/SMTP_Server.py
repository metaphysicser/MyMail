"""
-*- coding: utf-8 -*-
@Time    : 2021/11/9 17:29
@Author  : 夕照深雨
@File    : SMTP_Server.py
@Software: PyCharm

Attention：

"""
import smtpd
import asyncore
import logging
from Log.Log import Logger
import email.utils
from DAO.DAO_transaction_records import DAO_transaction_records

logger = Logger("./Log/SMTPServer_history.log", logging.DEBUG, __name__).getlog()


# 可以添加附件进行更改

class CustomSMTPServer(smtpd.SMTPServer):
    """
    SMTP 服务器，监听1025端口，接受来自他人投递的邮件

    """

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        logger.info("接收到来自 ip {} 的邮件，邮件发往 {}， 邮件来自 {}".format(peer[0], mailfrom, rcpttos))
        msg = email.message_from_bytes(data)
        target = email.utils.parseaddr(msg.get('to'))[1]
        source = email.utils.parseaddr(msg.get('from'))[1]
        content = msg["subject"]
        d = DAO_transaction_records()
        d.insert(source, target, content)


if __name__ == "__main__":
    server = CustomSMTPServer(('127.0.0.1', 587), None)
    asyncore.loop()
