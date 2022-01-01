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

conn = imaplib.IMAP4(port = 143,host = 'localhost')
print(1)
conn.login("zpl@qq.com","10")
conn.select()
type_, data = conn.search(None, 'ALL')
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
