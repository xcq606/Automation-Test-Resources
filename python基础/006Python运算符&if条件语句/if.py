# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/5/21
email: kinson.xie@cathaypacific.com
=========================================
"""
"""
条件判断
逻辑：python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块
其中判断条件成立时True，则执行后面的语句，执行内容可以多行，通过缩进表示执行范围，else为可选语句，判断条件为False执行

Python程序语言指定任何非0和非空（None）值为True，0或者None为False
比如说0，None，空字典，空列表都会被认为是False

if 条件：
    条件成立，执行此处代码
else：
    条件不成立，执行此处代码
"""
"""
通过条件判断设计一个登录小程序
账号为{'user':'kinson', 'password':'123456'}
输入账号 输入密码
判断账号是否正确，密码是否正确
账号或密码不正确，提示（登录失败，账号或密码不正确！）
账号密码正确提示（登录成功！）
"""
user_info = {'user':'kinson', 'password':'123456'}
username = input("请输入账号：")
password = input("请输入密码：")
if username == user_info['user'] and password == user_info['password']:
    print("登录成功！")
else:
    print("登录失败，账号或密码不正确！")
