# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/5/27
email: kinson.xie@cathaypacific.com
=========================================
"""
import random

# 1.输出99乘法表
# for i in range(1,10):
#     for j in range(1, i+1):
#         print("{} x {} = {}\t".format(j, i, i*j), end='')
#     print()

# 2.for循坏对列表中的数据排序，利用for循环，完成a=[1,7,4,89,34,2]从小到大排序（不使用列表的sort方法）
# a=[1,7,4,89,34,2]
# for i in range(0, len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# 3.有1 2 3 4 这4个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数，分别是什么
# num_expected = 0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and a!=c and b!=c:
#                 print("{}{}{}".format(a,b,c))
#                 num_expected += 1
# print("互不相同且无重复数字的3位数有{}个".format(num_expected))

# 4.石头剪刀布任务，游戏一轮出拳后进入下一轮，可以手动结束游戏，结束游戏后打印本轮游戏的胜率
# print("-----石头剪刀布游戏开始-----")
# count_win = 0
# count_sum = 0
# count_dogfall = 0
# while True:
#     print("请按照以下提示出拳：")
#     print("石头【1】 剪刀【2】 布【3】 结束游戏【0】")
#     list = ['石头','剪刀','布']
#     user_input = int(input("请输入你的选项："))
#     if user_input == 0:
#         print("游戏结束，本轮游戏您玩了{}把，赢了{}把，平局{}把，胜率为{:.2%}".format(count_sum, count_win, count_dogfall, count_win/count_sum))
#         break
#     computer_input = random.randint(1,3)
#     if 1 <= user_input <= 3:
#         count_sum += 1
#         if user_input == computer_input:
#             print("您的出拳为{}，电脑出拳{}，平局！".format(list[user_input-1], list[computer_input-1]))
#             count_dogfall += 1
#         elif (user_input - computer_input) == -1 or (user_input - computer_input) == 2:
#             print("您的出拳为{}，电脑出拳{}，您胜利了！".format(list[user_input-1], list[computer_input-1]))
#             count_win += 1
#         else:
#             print("您的出拳为{}，电脑出拳{}，您输了！".format(list[user_input-1], list[computer_input-1]))
#     else:
#         print("您的出拳有误，请重新出拳！")

# 5.图书馆管理系统功能完善
'''
说明：每一本图书包含三条信息，图书编号，图书名称，存放位置
添加：依次输入图书编号，图书名，图书位置进行添加
删除：输入书名，删除图书
显示所有书籍：显示出所有书本信息（分行显示，每行显示一本）
查询图书
修改图书
'''

book_list = []

while True:
    user_info = {'user':'kinson', 'password':'123456'}
    print("=欢迎来到图书馆管理系统=")
    username = input("请输入账号：")
    password = input("请输入密码：")
    if username == user_info['user'] and password == user_info['password']:
        print("登录成功！")
        print("=欢迎进入图书馆管理系统菜单=")
        while True:
            print("[1]: 添加图书")
            print("[2]: 修改图书")
            print("[3]: 删除图书")
            print("[4]: 查询图书")
            print("[5]: 退出")
            menu_num = input("请输入您的选项：")
            if menu_num == '1':
                book = {}
                book['id'] = input("请输入图书编号：")
                book['name'] = input("请输入图书名称：")
                book['position'] = input("请输入图书位置：")
                book_list.append(book)
                print("添加成功，返回主菜单")
            elif menu_num == '2':
                pass
            elif menu_num == '3':
                book_name = input("请输入删除的书名：")
                for book in book_list:
                    if book_name == book['name']:
                        book_list.remove(book)
                        print("删除成功，返回主菜单")
                        break
                else:
                    print("很抱歉，没有该书本信息！")
                    print("返回主菜单")
            elif menu_num == '4':
                book_count = len(book_list)
                if book_count == 0:
                    print("当前系统没有任何书籍，返回菜单页面")
                else:
                    print("当前系统共有{}本书籍，具体信息如下：".format(book_count))
                    for book in book_list:
                        print("编号{} 书名{} 位置{}".format(book['id'], book['name'], book['position']))
                    print("查询完成，返回主菜单")
            elif menu_num == '5':
                print("退出图书馆管理系统")
                break
            else:
                print("请输入正确的选项，蟹蟹！")
        break
    else:
        print("登录失败，账号或密码不正确！请重新输入~_~！")