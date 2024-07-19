# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/4/28
email: kinson.xie@cathaypacific.com
=========================================
"""

# 字符串定义， 单引号，双引号，三引号， str()
str_1 = ''
str_2 = ""
str_3 = """"""
str_4 = None
# print(type(str_1), type(str_2), type(str_3), type(str_4))
# <class 'str'> <class 'str'> <class 'str'> <class 'NoneType'>

# 字符串的常见操作
# 字符串拼接 +
str_5 = "Kinson"
str_6 = str_5 + "6061"
# print(str_6)

# 字符串的输出 print(), 输出多个不同的数据用逗号隔开
# print(str_5, str_6)

# 字符串转义 \n 换行，r''防止转义
str_7 = "kin\nson"
str_8 = "\""
str_9 = r"\""
# print(str_7, str_8, str_9)

# 下标取值
str_10 = "kinson"
# print(str_10[0])
# print(str_10[0:3])
# print(str_10[:3])
# print(str_10[3:])
# print(str_10[1:2])
# print(str_10[:])

# 字符串的常用方法
# join，字符串拼接
tuple_1 = ("hello", "kinson", "!")
# print(tuple_1)
# print(" ".join(tuple_1))

str_11 = "hello\n"
str_12 = "kinson"
# print(str_11.join(str_12))

# find，查找元素的位置（索引）
# print(str_12.find("k"))

# count，查找元素的个数
# print(str_12.count("k"))

# replace，替换字符
str_13 = "kkiissoonn"
# print(str_13.replace("k", "精神", 2))

# split，字符串分割
# print(str_13.split("i", 1))
# print(str_13.split("i"))

# format，格式化输出
kinson = "{} {} {}".format("kinson", "man", "18")
# print(kinson)

# upper，将字母转换成大写
# print("Kinson6061".upper())

# lower，将字母转换成小写
# print("Kinson6061".lower())

# 字符串格式化输出
# 传统的格式化输出%，这里回针对int，float，str去讲解格式化输出
# 输出整数 %d ???
# print("%dkinson123" % 1234)

# 输出浮点数 %f
# print("kinson %f" % 6)

# 指定输出小数点位数 %.2f
# print("kinson %.2f" % 6)

# 输出字符串 %s
# print("kinson %s" % "nice to meet you")

# 字符串截取 %.2s
# str_14 = "hello"
# print("kinson %.3s" % str_14)

# format格式化输出
# 相对基本格式化输出采用 %的方法，format()功能更强大，该函数把字符串当成一个模板，使用大括号 {} 作为特殊字符代替 %
# 常见使用方法
# 不指定序号，自动去匹配 {}
# print("{} {} {}".format("hello", "world", "kinson"))

# 指定序号去匹配{0}{1}
# print("{0} {2} {1}".format("hello", "world", "kinson"))

# 指定同一个序号去匹配{1}{1}
# print("{2} {2} {2}".format("hello", "world", "kinson"))

# 保留两位小数
# print("{:.2f} {}".format(123, "kinson"))

# 百分比形式显示
# print("{:.2%}".format(1))
