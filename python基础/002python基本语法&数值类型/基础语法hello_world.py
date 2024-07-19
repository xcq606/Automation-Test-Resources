# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/4/21
email: kinson.xie@cathaypacific.com
=========================================
"""
import keyword

print("hello python")

print(keyword.kwlist)

# 多行语句 - \
print("hello\
python")

# 多行语句 - '''
print('''hello 
kin
son''')

# 多行语句 - """
print("""hello 
kin
son‘s""")

name = input("what is your name: ")
print("nice to meet you, ", name)

# 行内注释1
# 行内注释2

'''
多行注释
文档/函数说明
'''

"""
推荐
多行注释
文档/函数说明
"""

item_one, item_two, item_three = "kinson", "606", "1.01"
total = item_one + \
        item_two + \
        item_three

print(total)
