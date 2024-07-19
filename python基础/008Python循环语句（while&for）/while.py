# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/5/21
email: kinson.xie@cathaypacific.com
=========================================
"""
import time

"""
惹老婆生气了，要跪搓衣板100遍
"""
i=0
while i<100:
    i += 1
    # print("老婆我错了，跪搓衣板第{}遍".format(i))

"""
实现1-100相加
"""
i = 0
sum = 0
while i<=100:
    i += 1
    sum += i
# print(sum)

"""
登录小程序集成循环
"""
# while True:
#     user_info = {'user':'kinson', 'password':'123456'}
#     username = input("请输入账号：")
#     password = input("请输入密码：")
#     if username == user_info['user'] and password == user_info['password']:
#         print("登录成功！")
#         break
#     else:
#         print("登录失败，账号或密码不正确！请重新输入~_~")

"""
break 结束循环
continue 中止本轮循环，进行下一个循环
"""
# j = 0
# while j < 10:
#     j += 1
#     if j == 5:
#         continue
#     print("这是第{}遍".format(j))

"""
li = [1,2,3,55,66,10,11,4,67]
输出大于10的元素
"""
li = [1,2,3,55,66,10,11,4,67]
li_1 = []
i = 0
while i < len(li):
    if li[i] >= 10:
        li_1.append(li[i])
    i += 1
print(li_1)