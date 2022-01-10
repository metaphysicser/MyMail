"""
-*- coding: utf-8 -*-
@Time    : 2022/1/11 1:26
@Author  : 夕照深雨
@File    : judge_input.py
@Software: PyCharm

Attention：

"""
import re

def judge_input(password):
    if len(password)<8:
        return '不够8个字符'
    #下面这行条件的意思是：如果密码里所有的字符都符合条件，也就是都在我正则表达式的序列里，那么findall得到的列表长度和密码本身的长度就应该是一样的；如果密码里有不符合条件的字符，那么findall得到的列表长度就会小于密码的长度（相差的部分就是那些非法字符）
    elif len(re.findall('[A-Za-z0-9_]',password))<len(password):
        return '有非法字符'
    else:
        #first代表大写字母类型，如果密码里没有大写字母，那么search就会返回None，我们就把这种字符类型记为0，也就是不存在大写字母。否则，记为1，也就是存在大写字母。后面对小写字母和数字的处理是同样的道理。
        first=re.search('[A-Z]',password)
        if first==None:
            num1=0
        else:
            num1=1
        second=re.search('[a-z]',password)
        if second==None:
            num2=0
        else:
            num2=1
        third=re.search('[0-9]',password)
        if third==None:
            num3=0
        else:
            num3=1
        #下面是统计字符类型总共有多少，不少于2则符合条件，否则就要提示用户字符类型单一。
        if num1+num2+num3>=2:
            return True
        else:
            return '字符类型单一，数字、大写字母和小写字母至少要有两种'

