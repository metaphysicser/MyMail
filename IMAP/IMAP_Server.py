"""
-*- coding: utf-8 -*-
@Time    : 2021/11/4 10:40
@Author  : 夕照深雨
@File    : IMAP_Server.py
@Software: PyCharm

Attention：

"""
import socket

print("Server is starting")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 143))  # 配置soket，绑定IP地址和端口号
sock.listen(5)  # 设置最大允许连接数，各连接和server的通信遵循FIFO原则
print("Server is listenting port 8001, with max connection 5")
while True:  # 循环轮询socket状态，等待访问

    connection, address = sock.accept()
    print(connection, address)
    try:
        connection.settimeout(50)
        connection.send('* OK IMAP4rev1 server ready\r\n'.encode())
        connection.send('* CAPABILITY IMAP4rev1 STARTTLS AUTH=GSSAPILOGINDISABLED\r\n'.encode())
        # connection.send(
        #     'a01 OK CAPABILITY Completed\r\n'.encode())
        # 获得一个连接，然后开始循环处理这个连接发送的信息
        '''
        如果server要同时处理多个连接，则下面的语句块应该用多线程来处理，
        否则server就始终在下面这个while语句块里被第一个连接所占用，
        无法去扫描其他新连接了，但多线程会影响代码结构，所以记得在连接数大于1时
        下面的语句要改为多线程即可。
        '''
        while True:

            buf = connection.recv(1024).decode('utf-8')
            print(buf)

            if buf.split()[1] == "CAPABILITY":
                connection.send('* CAPABILITY IMAP4rev1 STARTTLS AUTH=GSSAPILOGINDISABLED\r\n'.encode())
                connection.send((buf.split()[0] +' OK CAPABILITY Completed\r\n').encode())
            else:
                print("close")
                # break  # 退出连接监听循环
    except socket.timeout:  # 如果建立连接后，该连接在设定的时间内无数据发来，则time out
        print('time out')

    print("closing one connection")  # 当一个连接监听循环退出后，连接可以关掉
    connection.close()
