"""
如何使用模块
    导入模块：
        1. import 模块名1， 模块名2……
        使用方式：
            模块名.变量
            模块名.函数名（参数）
            模块名.类

        2. 导入模块中的数据
             from 模块 import 变量，函数，类
        使用方式：直接使用

"""
# 方式1
# import mypro_oop.myadd
# print(mypro_oop.myadd.x)
# 方式2
from mypro_oop import add
print(add(4, 5))
