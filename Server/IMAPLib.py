"""
-*- coding: utf-8 -*-
@Time    : 2021/11/6 10:47
@Author  : 夕照深雨
@File    : IMAPLib.py
@Software: PyCharm

Attention：

"""

import re
import logging
from logging.handlers import RotatingFileHandler

logger_map = {

}


# 获取指定房间的日志记录器
def get_logger(desk):
    if desk not in logger_map.keys():
        # 获取日志记录器
        logger_ = logging.getLogger(desk)
        logger_.setLevel(logging.INFO)

        # 滚动日志处理器
        handler = RotatingFileHandler(desk + '.log', 'a', 5024 * 1024, 1000000, 'utf8')
        handler.setLevel(logging.INFO)

        # 创建一个格式器formatter并将其添加到处理器handler
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')
        handler.setFormatter(formatter)

        # 为日志器logger添加上面创建的处理器handler
        logger_.addHandler(handler)
        logger_map[desk] = logger_
    return logger_map[desk]

logger = get_logger("history")

command_format = re.compile(r'((?P<tag>[0-9a-zA-Z]+) (?P<data>[^\s]*))( (?P<arg>.*))*',
                            re.ASCII)  # 客户端命令的正则表达式,tag只能由数字和字母组成

#  命令和其对应的有效状态

Commands = {
    # name            valid states
    'APPEND': ('AUTH', 'SELECTED'),
    'AUTHENTICATE': ('NONAUTH',),
    'CAPABILITY': ('NONAUTH', 'AUTH', 'SELECTED', 'LOGOUT'),
    'CHECK': ('SELECTED',),
    'CLOSE': ('SELECTED',),
    'COPY': ('SELECTED',),
    'CREATE': ('AUTH', 'SELECTED'),
    'DELETE': ('AUTH', 'SELECTED'),
    'DELETEACL': ('AUTH', 'SELECTED'),
    'ENABLE': ('AUTH',),
    'EXAMINE': ('AUTH', 'SELECTED'),
    'EXPUNGE': ('SELECTED',),
    'FETCH': ('SELECTED',),
    'GETACL': ('AUTH', 'SELECTED'),
    'GETANNOTATION': ('AUTH', 'SELECTED'),
    'GETQUOTA': ('AUTH', 'SELECTED'),
    'GETQUOTAROOT': ('AUTH', 'SELECTED'),
    'MYRIGHTS': ('AUTH', 'SELECTED'),
    'LIST': ('AUTH', 'SELECTED'),
    'LOGIN': ('NONAUTH',),
    'LOGOUT': ('NONAUTH', 'AUTH', 'SELECTED', 'LOGOUT'),
    'LSUB': ('AUTH', 'SELECTED'),
    'MOVE': ('SELECTED',),
    'NAMESPACE': ('AUTH', 'SELECTED'),
    'NOOP': ('NONAUTH', 'AUTH', 'SELECTED', 'LOGOUT'),
    'PARTIAL': ('SELECTED',),  # NB: obsolete
    'PROXYAUTH': ('AUTH',),
    'RENAME': ('AUTH', 'SELECTED'),
    'SEARCH': ('SELECTED',),
    'SELECT': ('AUTH', 'SELECTED'),
    'SETACL': ('AUTH', 'SELECTED'),
    'SETANNOTATION': ('AUTH', 'SELECTED'),
    'SETQUOTA': ('AUTH', 'SELECTED'),
    'SORT': ('SELECTED',),
    'STARTTLS': ('NONAUTH',),
    'STATUS': ('AUTH', 'SELECTED'),
    'STORE': ('SELECTED',),
    'SUBSCRIBE': ('AUTH', 'SELECTED'),
    'THREAD': ('SELECTED',),
    'UID': ('SELECTED',),
    'UNSUBSCRIBE': ('AUTH', 'SELECTED'),
    'UNSELECT': ('SELECTED',),
}


class IMAP:
    """
    IMAP协议服务端响应

    """
    class error(Exception):
        pass  # 逻辑错误

    class abort(error):
        pass  # 连接错误

    class readonly(abort):
        pass  # 只读模式

    def __init__(self):
        self.state = "LOGOUT"

    def handle_command(self, command):
        try:
            if not command:
                logger.error("接受命令为空")
                return ["* BAD Command!"]
            match = command_format.match(command)
            if match != None:
                tag = match.group("tag")
                data = match.group("data")
                arg = match.group("arg")
                data = data.upper()
                if data not in Commands.keys():
                    logger.error(command + "中的" + data + "命令不存在")
                    return ["* BAD Command!"]

                return self.command_response(tag, data, arg)
            else:
                logger.error(command + " 是一个不符合格式的命令")
                return ["* BAD Command!"]
        except Exception as e:
            pass

    def command_response(self, tag, name, arg):
        """
        命令响应格式

        :param tag: 标志
        :param name: 名称
        :param arg: 参数
        :return:
        """
        if self.state not in Commands[name]:
            logger.info("command %s illegal in state %s, "
                        "only allowed in states %s" %
                        (name, self.state,
                         ', '.join(Commands[name])))
            return [tag + " NO Unauthorized"]

        if name == "CAPABILITY":
            return self.get_capabilities(tag, name)
        elif name == "LOGIN":
            return self.login(tag, arg)

    def get_capabilities(self, tag, name):
        """
        获得权限

        :param tag:
        :param name:
        :return:
        """
        res = []
        self.state = "NONAUTH"
        res.append("* CAPABILITY IMAP4rev1 AUTH=GSSAPI AUTH=PLAIN AUTH = LOGIN")
        res.append(tag + " OK CAPABILITY Completed")
        return res

    def login(self, tag, arg):
        """
        验证账号密码进行登陆

        :param tag:
        :param arg:
        :return:
        """
        return [tag + " OK LOGIN completed"]


if __name__ == "__main__":
    match = command_format.match("JDDE0 CAPABILITY zpl 010720")
    print(match.group("tag"))
    print(match.group("data"))
    print(match.group("arg"))
