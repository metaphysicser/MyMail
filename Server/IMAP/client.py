"""
-*- coding: utf-8 -*-
@Time    : 2021/11/4 10:46
@Author  : 夕照深雨
@File    : IMAP_CLient.py
@Software: PyCharm

Attention：

"""

import socket
import time
import imaplib
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('localhost', 8001))

conn = imaplib.IMAP4_SSL(host = 'imap.qq.com')
print(1)
print(conn.login("zpl010720@qq.com","esnkoqfbkduucejh"))
print(conn.select())
type_, data = conn.fetch("1", '(RFC822)')
print(type_)
print(data)
# print(2)
# ret = conn.getquota(root='xxoo@sex.com')
# flag = '1'
# while True:
#     time.sleep(3)
#     print('send to server with value: ' + flag)
#     sock.send(flag.encode())
#     print(sock.recv(1024))f
#     flag = (flag == '1') and '2' or '1'  # change to another type of value each time
#
#
# client = socket.socket()
#
# client.connect(('localhost', 143))
#
# while True:
#     upData = client.recv(1024)
#     print(upData)
#
#     msg = input('>>:').strip()
#     if not msg:
#         continue
#     else:
#         client.send(msg.encode('utf-8'))
