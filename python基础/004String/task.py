# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/5/10
email: kinson.xie@cathaypacific.com
=========================================
"""
# 1. 定义字符串I‘m Kinson, I love python
str_1 = "I‘m Kinson, I love python"
# print("定义字符串I‘m Kinson, I love python: ", str_1)

# 2. 将字符串前后的空格去掉，把Jason替换为Kison
str_2 = "   Jason is a best superman in the world!   "
str_2 = str_2.replace("Jason", "kinson")
# str_2 = str_2.strip()
# str_2 = str_2.rstrip()
# str_2 = str_2.lstrip()
# print("str_2:", str_2)

# 3. 现在有个元祖tuple_1,通过代码转换为字符串hello kinson！
tuple_1 = ("hello", "kinson", "!")
# print(" ".join(tuple_1).replace(" !", "!"))

# 4. 在控制台依次提示用户输入：姓名，年龄，性别按照以下格式输出
"""
*********************
个人信息展示：
姓名：姓名
年龄：年龄
性别：性别c
*********************
"""
name = input("请输入姓名：")
age = input("请输入姓名：")
gender = input("请输入姓名：")
print("*********************")
print("姓名：{}".format(name))
print("年龄：{}".format(age))
print("性别：{}".format(gender))
print("*********************")
