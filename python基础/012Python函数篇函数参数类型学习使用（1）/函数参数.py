# -*-coding:utf8-*-
"""
=========================================
author: xcq
time: 2024/6/19
email: kinson.xie@cathaypacific.com
=========================================
"""


# a, b 为形式参数， 调用的时候11,22为实际参数
def add_num(a, b, c):
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    return a + b + c


# 参数传入的接受规则
# 位置参数，按照位置传入，a=11，b=22
print(add_num(11, 22, 33))
# 关键字参数，通过关键字（形参）指定传入
print(add_num(a=22, c=11, b=33))
# 混合传入,不能起冲突(位置参数写在前面，不能放在关键字参数后面，否则会报错（Positional argument after keyword argument）)
print(add_num(111, b=222, c=111))

# 根据函数定义的形参进行分类
# 必须参数 add_num必须穿abc，多或者少都不行
print(add_num(11, 22, 33))
# 默认参数（缺省参数）
def add_num_1(a, b, c=0):
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    return a + b + c
add_num_1(11,22)
add_num_1(11,22,33)
# 不定长参数
# *args 可以不传，也可以传多个，以元祖的形式保存
def add_num_args(a, b, c, *args):
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("*args: ", args)
print("args", add_num_args(1,2,3,4,5,6,7,8,9))
# **kwargs 传入的是字典
def add_num_kwargs(a, b, c, **kwargs):
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("**kwargs: ", kwargs)


add_num_kwargs(1,2,3, d=5, k=1000)
