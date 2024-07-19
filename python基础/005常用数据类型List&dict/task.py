# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/5/19
email: kinson.xie@cathaypacific.com
=========================================
"""
# 1、字符串、元组、列表为什么被称为序列类型，说明元祖和列表的区别
# 序列类型：因为它们是有顺序的，可以通过下标索引获取元素
# 元祖是不可变类型，定义后不可以改变内部结构
# 列表是可变类型。定义后内部的元素是可以改变的

# 2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或者7，打印输出“周末”
# while True:
#     num = int(input("请输入1-7其中一个数字: "))
#     if num == 6 or num == 7:
#         print("周末")
#         break
#     if 1<= num <=5:
#         print("星期{}".format(num))
#         break
#     else:
#         print("您输入的数字为{}，请重新输入1-7，蟹蟹！".format(num))

# list_1 = ["1", "2", "3", "4", "5", "末", "末"]
# num = int(input("请输入1-7之间的数字："))
# print("今天是周{}".format(list_1[num - 1]))

# 3、现在有一个列表li2 = [1, 2, 3, 4, 5]
# li2 = [1, 2, 3, 4, 5]
# 3.1通过相关的操作改成li2 = [0, 1, 2, 3, 66, 4, 5, 11, 22, 33]
# li2.insert(0, 0)
# li2.insert(li2.index(4), 66)
# li2.extend([11,22,33])
# print(li2)

# 3.2对li2进行排序处理
# li2.sort()
# print(li2)
# li2.sort(reverse=True)
# print(li2)

# 3.3写出删除列表中元素的方法，并说明每个方法的作用
# pop 指定下标删除，不写默认为最后一个
# li2.pop()
# print(li2)
# li2.pop(li2.index(22))
# print(li2)

# remove 删除指定的值
# li2.remove(66)
# print(li2)

# clear 清空列表
# li2.clear()
# print(li2)

# del 根据下标删除，无下标则删除整个列表，从内存中删除
# del(li2[0])
# del(li2)
# print(li2) # NameError: name 'li2' is not defined

# 4.切片
# 4.1 - li = [1, 2, 3, 4, 5, 6, 7, 8, 9], 预期切片[3, 6, 9]
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(li[2::3])

# 4.2 - s = 'python java php', 预期切片java
# s = 'python java php'
# print(s.split(" ")[1])
# print(s[7:11])

# 4.3 - tu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'), 预期切片[b, g]
# tu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# print(list(tu[-2:-8:-5]))

# 5.写出列表添加数据的所有方法
# append()
# insert(下标，值)
# extend([1,2,3])
