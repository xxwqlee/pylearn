"""
    复习模块导入
    f-string 新的字符串格式化方法
"""

import hdd.day3
from hdd import IsNum, Triangle

hdd.day3.fib_num(9)
IsNum.is_prime(57233)
t1 = Triangle(44, 55, 88)
print('{}\t{}'.format(t1.perimeter(), t1.area()))
# f-string 的用法
print(f'{t1.perimeter()}\t{t1.area()}')
a, b = 3, 5
print(f'a + b = {a + b}')
