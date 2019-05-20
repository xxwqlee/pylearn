"""
    复习模块导入
"""

import hdd.day3
from hdd import IsNum, Triangle

hdd.day3.fib_num(9)
IsNum.is_prime(57233)
t1 = Triangle(44, 55, 88)
print('{}\t{}'.format(t1.perimeter(), t1.area()))
