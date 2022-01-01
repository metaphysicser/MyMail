"""
-*- coding: utf-8 -*-
@Time    : 2021/11/9 17:53
@Author  : 夕照深雨
@File    : SMTP_Client.py
@Software: PyCharm

Attention：

"""

import smtplib
import email.utils
from email.mime.text import MIMEText

# 创建消息
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', 587)
server.set_debuglevel(True)  # 显示与服务器的通信
try:
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    msg.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()

