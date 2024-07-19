# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/4/25
email: kinson.xie@cathaypacific.com
=========================================
"""
# 问题1：如果要存储全班所有人的姓名，怎么存储？
# 问题2：如果要存储全班同学的年龄和姓名，怎么存储？

# 字典 散列类型（内部元素无下标，无序）{key:value, key:value}
# key为索引，为不可变类型（string、元祖，number，通常用string）
dic_1 = {"name": "Kinson Xie", "age": "18", "gender": "man"}
print(dic_1)

# 集合,内部不存在重复数据,可以用来去重
# set_1 = set() # 空集合
# set_1 = {1, 2, 3}
# print(set_1)
# print(type(set_1))
# list_1 = [11,11,22,22,33,33]
# print(set(list_1))

# 字典 {}空的为字典
# dic_1 = {}
# print(type(dic_1))

# 增删查改
# 增：通过指定键去添加对应的值 dic[key]=value, 更新或者增加，有对应的键则改，无则增加
# update() 将一个字典的所有元素更新到另一个字典中 dic.update({'a':1, 'b':2}) 可以理解为添加多个元素
dic_2 = {"name": "Kinson Xie", "age": "18", "gender": "man"}
dic_2["name"] = "Kinson"
dic_2["high"] = 180
print(dic_2)
dic_2.update({'a':1, 'b':2})
print(dic_2)

# 改：通过指定键去修改对应的值 dic[key]=value
dic_2['age'] = 34
print(dic_2)

# 删：
# pop() 删除指定的键，删除的键如果不存在回报错（避免报错可以添加默认值） dic.pop(key)
# popitem() 删除一个键值对，删除最后一个添加的元素 dic.popitem() py3.7之前的逻辑是随机删除
# 关键字del 删除键 del dic(key)
# dic_2.pop("aaa") # KeyError: 'aaa'
dic_2.pop('a')
print(dic_2)
dic_2.popitem()
print(dic_2)
# del dic_2 #从内存中删除整个字典，
# print(dic_2) #NameError: name 'dic_2' is not defined. Did you mean: 'dic_1'?
del dic_2['age']
print(dic_2)

# 查
# get() 获取键对应的值 dic.get(key) 不存在时不会报错
# keys() 获取所有的键，可以用list将结果转换为列表
# values() 获取所有的值，可以用list将结果转换为列表
# items() 获取所有的键值对，可以用list将结果转换为列表，列表中每个键值对组成一个元组
print(dic_2.get("name"))
print(list(dic_2.keys()))
print(list(dic_2.values()))
print(list(dic_2.items()))
