# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/5/21
email: kinson.xie@cathaypacific.com
=========================================
"""

"""
图书馆管理系统设计
"""
# 用户列表
user_list = [{'user': 'kinson', 'password': '123456'}, {'user': 'yoyo', 'password': '123456'}]
# 图书列表
book_list = []


def register():
    while True:
        username = input("请输入账号：")
        password = input("请输入密码：")
        confirm_password = input("请再次输入密码：")
        for user in user_list:
            if user['user'] == username:
                print("用户已存在，请重新输入！")
                break
        else:
            if password == confirm_password:
                new_user = {'user': username, 'password': password}
                user_list.append(new_user)
                print("注册成功！")
                break
            else:
                print("您两次输入的密码不一致！")


def login():
    username = input("请输入账号：")
    password = input("请输入密码：")
    for user in user_list:
        if user['user'] == username and user['password'] == password:
            return {'code':1, 'msg': '登录成功'}
    else:
        return {'code':0, 'msg': '登录失败，账号或密码不正确'}


def print_menu():
    print("[1]: 添加图书")
    print("[2]: 修改图书")
    print("[3]: 删除图书")
    print("[4]: 查询图书")
    print("[5]: 显示所有图书")
    print("[6]: 退出系统")


def add_book():
    pass


def update_book():
    pass


def del_book():
    pass


def find_book():
    pass


def all_book():
    pass


def main():
    # 控制整个程序的运行流程
    while True:
        print("------=<欢迎来到图书馆管理系统>=-------")
        print("【1】登录，【2】注册 【3】退出系统")
        num = input("请输入选项：")
        if num == '1':
            # 登录
            res = login()
            if res['code'] == 1:
                print("登录成功，进入主菜单")
                while True:
                    print_menu()
                    num_1 = input("请输入您的选项：")
                    if num_1 == '1':
                        add_book() # 添加图书
                    elif num_1 == '2':
                        update_book() # 修改图书
                    elif num_1 == '3':
                        del_book() # 删除图书
                    elif num_1 == '4':
                        find_book() # 查询图书
                    elif num_1 == '5':
                        all_book() # 显示所有图书
                    elif num_1 == '6':
                        break # 退出
                    else:
                        print("您输入的选项有误，请重新输入！")
                break
            else:
                print("您输入的账号或密码有误！")
        elif num == '2':
            register() # 注册
            pass
        elif num == '3':
            print("------=<欢迎再次来到图书馆管理系统>=-------")
            print("------再见-------")
            break
        else:
            print("您的输入有误，请重新输入！")


if __name__ == '__main__':
    main()
