"""
-*- coding: utf-8 -*-
@Time    : 2022/1/6 23:35
@Author  : 夕照深雨
@File    : Send_Mail.py
@Software: PyCharm

Attention：

"""
import logging
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from Server.Log.Log import Logger

logger = Logger("../Log/server_history.log", logging.DEBUG, __name__).getlog()
Attachment_path = "../Attachment/"
SERVER_PORT = {"smtp.qq.com": 465}


class SendMail(object):
    """
    实现邮件的发送功能
    """

    def __init__(self, receiver = '', sender_name = '', title = '', content = '', sys_sender = '', sys_pwd = '', file_list= []):
        self.receiver = receiver  # 发送地址
        self.sender_name = sender_name  # 发送人用户名
        self.title = title  # 标题
        self.content = content  # 发送内容
        self.sys_sender = sys_sender  # 系统账户
        self.sys_pwd = sys_pwd  # 系统账户密码
        self.file_list = file_list
        
    def verify_account(self, account, password):
        """
        验证邮箱密码是否正确
        Returns:

        """
        try:
            target_server = "smtp." + account.split("@")[1]
            server = smtplib.SMTP_SSL(target_server, SERVER_PORT[target_server], timeout=10)
            server.login(account, password)
            return True
        except:
            return False
        

    def send_email(self):
        """
        使用smtp协议登陆用户邮箱发送邮件
        Returns:

        """
        try:
            target_server = "smtp." + self.sys_sender.split("@")[1]
            server = smtplib.SMTP_SSL(target_server, SERVER_PORT[target_server], timeout=10)
            server.login(self.sys_sender, self.sys_pwd)
            msg = self.message(self.file_list)
            # 发送邮件
            if msg is not None:
                server.sendmail(self.sys_sender, [self.receiver, ], msg.as_string())
                server.quit()
            else:
                raise Exception("无法构建邮件正文")
        except Exception as e:
            logger.error("用户{}发往{}的邮件发送失败".format(self.sender_name, self.receiver))
            logger.error(e)
            return False

        logger.info("用户{}发往{}的邮件发送成功".format(self.sender_name, self.receiver))
        return True

    def message(self, file_list):
        """
        发送邮件
        :param file_list: 附件文件列表
        :return: bool
        """
        try:
            # 创建一个带附件的实例
            msg = MIMEMultipart()
            # 发件人格式
            msg['From'] = formataddr([self.sender_name, self.sys_sender])
            # 收件人格式
            msg['To'] = formataddr(["", self.receiver])
            # 邮件主题
            msg['Subject'] = self.title
            # 邮件正文内容
            msg.attach(MIMEText(self.content, 'plain', 'utf-8'))

            if len(file_list) != 0:
                for file_name, path_name in file_list.items():
                    # 构造附件
                    attach_part = MIMEApplication(open(Attachment_path+path_name, 'rb').read())
                    # filename表示邮件中显示的附件名
                    attach_part.add_header('Content-Disposition', 'attachment', filename='%s' % file_name)
                    msg.attach(attach_part)

            return msg

        except Exception as e:
            logger.error(e)
            return None


if __name__ == '__main__':
    mail = SendMail("zpl010720@qq.com", "zpl","测试邮件","测试内容","zpl010720@qq.com","esnkoqfbkduucejh",{"graweg":"1.txt"})
    mail.send_email()
