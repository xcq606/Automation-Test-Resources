# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/5/21
email: kinson.xie@cathaypacific.com
=========================================
"""

"""
li = [1,2,3,55,66,10,11,4,67]
输出大于10的元素
"""
li = [1,2,3,55,66,10,11,4,67]
li_1 = []
for li_element in li:
    if li_element >= 10:
        li_1.append(li_element)
print(li_1)