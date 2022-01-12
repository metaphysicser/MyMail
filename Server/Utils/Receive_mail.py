"""
-*- coding: utf-8 -*-
@Time    : 2022/1/12 1:00
@Author  : 夕照深雨
@File    : Receive_mail.py
@Software: PyCharm

Attention：

"""
from lxml.builder import unicode

user = 'zpl010720@qq.com'
passwd = 'esnkoqfbkduucejh'

from bs4 import BeautifulSoup
import imaplib, email
import base64
import sys
import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64
from email.header import Header



# *********接受邮件部分（IMAP）**********
# 处理接受邮件的类
class ReceiveMailDealer:

    # 构造函数(用户名，密码，imap服务器)
    def __init__(self, username, password):
        self.server = "imap." + username.split("@")[1]
        self.mail = imaplib.IMAP4_SSL(self.server)
        self.mail.login(username, password)
        self.select("INBOX")

    # 返回所有文件夹
    def showFolders(self):
        return self.mail.list()

    # 选择收件箱（如“INBOX”，如果不知道可以调用showFolders）
    def select(self, selector):
        return self.mail.select(selector)

    # 搜索邮件(参照RFC文档http://tools.ietf.org/html/rfc3501#page-49)
    def search(self, charset, *criteria):
        try:
            return self.mail.search(charset, *criteria)
        except:
            self.select("INBOX")
            return self.mail.search(charset, *criteria)

    # 返回所有未读的邮件列表（返回的是包含邮件序号的列表）
    def getUnread(self):
        return self.search(None, "Unseen")

    # 以RFC822协议格式返回邮件详情的email对象
    def getEmailFormat(self, num):
        data = self.mail.fetch(num, 'RFC822')
        if data[0] == 'OK':
            return email.message_from_string(data[1][0][1].decode('utf-8'),)
        else:
            return "fetch error"

    # 返回发送者的信息——元组（邮件称呼，邮件地址）
    def getSenderInfo(self, msg):
        name = email.utils.parseaddr(msg["from"])[0]
        deName = email.header.decode_header(name)[0]
        if deName[1] != None:
            name = unicode(deName[0], deName[1])
        address = email.utils.parseaddr(msg["from"])[1]
        return (name, address)

    # 返回接受者的信息——元组（邮件称呼，邮件地址）
    def getReceiverInfo(self, msg):
        name = email.utils.parseaddr(msg["to"])[0]
        deName = email.header.decode_header(name)[0]
        if deName[1] != None:
            name = unicode(deName[0], deName[1])
        address = email.utils.parseaddr(msg["to"])[1]
        return (name, address)

    # 返回邮件的主题（参数msg是email对象，可调用getEmailFormat获得）
    def getSubjectContent(self, msg):
        deContent = email.header.decode_header(msg['subject'])[0]
        if deContent[1] != None:
            return unicode(deContent[0], deContent[1])
        return deContent[0]

    '''判断是否有附件，并解析（解析email对象的part）
    返回列表（内容类型，大小，文件名，数据流）
    '''

    def parse_attachment(self, message_part):
        content_disposition = message_part.get("Content-Disposition", None)
        if content_disposition:
            dispositions = content_disposition.strip().split(";")
            if bool(content_disposition and dispositions[0].lower() == "attachment"):

                file_data = message_part.get_payload(decode=True)
                attachment = {}
                attachment["content_type"] = message_part.get_content_type()
                attachment["size"] = len(file_data)
                deName = email.header.decode_header(message_part.get_filename())[0]
                name = deName[0]
                if deName[1] != None:
                    name = unicode(deName[0], deName[1])

                attachment["name"] = name
                attachment["data"] = file_data
                '''保存附件
                fileobject = open(name, "wb")
                fileobject.write(file_data)
                fileobject.close()
                '''
                return attachment
        return None

    '''返回邮件的解析后信息部分
    返回列表包含（主题，纯文本正文部分，html的正文部分，发件人元组，收件人元组，附件列表）
    '''

    def getMailInfo(self, num):
        msg = self.getEmailFormat(num)
        attachments = []
        body = None
        html = None
        for part in msg.walk():
            attachment = self.parse_attachment(part)
            if attachment:
                attachments.append(attachment)
            elif part.get_content_type() == "text/plain":

                body = part.get_payload(decode=True)
            elif part.get_content_type() == "text/html":

                html = part.get_payload(decode=True)

        return {
            'subject': self.getSubjectContent(msg),
            'body': str(body,encoding = "utf8"),
            'html': str(html,encoding = 'utf8'),
            'from': self.getSenderInfo(msg),
            'to': self.getReceiverInfo(msg),
            'attachments': attachments
        }
    def getMailPartInfo(self, num):
        msg = self.getEmailFormat(num)
        attachments = []
        body = None
        html = None
        for part in msg.walk():
            attachment = self.parse_attachment(part)
            if attachment:
                attachments.append(attachment)
            elif part.get_content_type() == "text/plain":

                body = part.get_payload(decode=True)
            elif part.get_content_type() == "text/html":

                html = part.get_payload(decode=True)

                if html is not None:

                    html = base64.b64encode(html)

                    html = str(html)[2:-1]

        print(type(html), type(body))


        return {
            "subject": self.getSubjectContent(msg),
            'body': str(body, encoding = "utf8") if body is not None else None,
            'html': html,
            "from": self.getSenderInfo(msg),
            "to": self.getReceiverInfo(msg)
        }


if __name__ == '__main__':

    rml = ReceiveMailDealer(user,passwd)
    rml.select("Sent")
    status, num = rml.search("All")
    newlist=num[0].split()
    print(newlist)


    print(rml.getMailInfo(newlist[1])["html"])


