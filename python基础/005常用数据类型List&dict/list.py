# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/4/25
email: kinson.xie@cathaypacific.com
=========================================
"""

# 列表的定义
# 列表用[]号来标识
# 列表内部的元素可以是任意类型的
# 列表是使用最频繁的数据类型之一
list_1 = [1, 2, 'k', {"a":"1"}]
print(list_1)

# 列表的常见操作
# 下标索引取值：列表内部的元素是有顺序的，可以通过下标取值
list_2 = [1, 2, 'k', {"a":"1"}]
print(id(list_2))
print(list_2[0])
print(list_2[3])
print(list_2[1:3])
print(list_2[:3])

# 修改元素的值，可以通过下标修改元素的值
list_2[2] = 'kinson'
print(list_2)
print(id(list_2))

# 列表的方法
list_3 = [11, 22, "kinson", (1, 2, 3, 4), 1.11]
# 增：append、insert、extend
# append 添加在最后
list_3.append("hello")
# insert 根据下标插入，在索引 元素签名插入
list_3.insert(list_3.index("kinson"), "I am coming")
print(list_3)
# extend, 元素会被拆分 'p', 'y', 't', 'h', 'o', 'n'],
list_3.extend("python")
list_3.extend(("hello", "world"))
list_3.extend(["hello", "world"])
list_3.extend({"hello":"world"})
print(list_3)

# 删：pop、remove、clear、del
# pop 根据下标删除元素
list_3.pop(0)
print(list_3)
# remove 根据元素值删除元素
list_3.remove(22)
print(list_3)
# clear清空列表
list_3.clear()
print(list_3)
# del 从内存删除列表
list_del = [1, 2]
del list_del[0]
print("list_del: ", list_del)
del list_del
# print("list_del: ", list_del) # NameError: name 'list_del' is not defined


# 改：通过下标修改
list_3.append("kinson")
list_3[0] = "Kinson"
print(list_3)

# 查：index、count
list_4 = [11, 22, "kinson", (1, 2, 3, 4), 1.11, 11]
print(id(list_4))
len_list_4 = len(list_4)
print(list_4.index(11))
print(list_4.count(11))

# 其他：copy，reverse、sort
# sort排序
list_5 = [11,11,2,33,4,64,65776,33,2,41]
list_5.sort()
print("list sort(default(reverse=False)): ", list_5)
list_5.sort(reverse=True)
print("list sort(reverse=True): ", list_5)
# 字符串和元祖等不可变类型不能使用sort()
# sort排序 一般用于纯数值类型
# 字符串排序规则遵循ASCII编码（没实际意义）

# reverse反序处理
list_6 = [1, 22, 333, 4, 555, 666]
list_7 = ["a", "b", "c", "d"]
list_6.reverse()
list_7.reverse()
print("reverse反序处理: ", list_6)
print("reverse反序处理: ", list_7)

# copy
list_8 = [1, 2, 3]
list_9 = list_8
list_10 = list_8.copy()
list_8.append(4)
print(id(list_8), id(list_9), id(list_10))
print(list_8, list_9, list_10)
