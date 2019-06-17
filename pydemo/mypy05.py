# 函数定义和使用
import math
import copy


def add(a, b):
    """two num sum"""
    return a + b


print(add(3, 5))
x = math.inf
print(x)
# 参数的传递
a = [10, 20]
print(id(a))


def apd(m):
    print(id(m))
    m.append(300)
    print(id(m))


apd(a)
print(a)
print('*******************')
# 测试深浅拷贝

l_1 = [10, 20, [5, 6]]
l_2 = copy.copy(l_1)

print(l_1, end='l1\n')
print(l_2, end='l2\n')

l_2.append(22)
l_2[2].append(7)
print('copy')
print(l_1, end='l1\n')
print(l_2, end='l2\n')

l_3 = copy.deepcopy(l_1)

print(l_1, end='l1\n')
print(l_3, end='l3\n')
l_3.append(22)
l_3[2].append(7)
print('deepcopy')
print(l_1, end='l1\n')
print(l_3, end='l3\n')
# 不可变对象的参数传递包含子对象的引用

t_a = (10, 20, [5, 6])
print('a:', t_a)
print('id of a:', id(t_a))


def trans(m):
    print('id of m', id(m))
    m[2][0] = 666
    print(m)
    print('id of m', id(m))


trans(t_a)
print(t_a)
