# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/4/25
email: kinson.xie@cathaypacific.com
=========================================
"""

# 元组定义，元组内部的数据，支持数字，字符串，嵌套元组
tuple_1 = (1, 22, 3, ("kinson", "love"))
tuple_2 = ()
tuple_3 = (1,)
print("{} {} {}".format("tuple_1", type(tuple_1), tuple_1))

# 元组的常见操作
# 下标取值
print(tuple_1[0])

# count 查找元素个数
print(tuple_1.count(1))

# index 查找元素下标
print(tuple_1[3].index("kinson"))
