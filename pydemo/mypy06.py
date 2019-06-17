# 多种参数类型的使用


def prt1(a, b, c, d):
    print('a =', a, 'b =',  b, 'c =', c, 'd =', d)


def prt2(a, b, c=10, d=20):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d)


# 位置参数
prt1(1, 3, 4, 5)
# 命名参数
prt1(a=10, b=30, c=40, d=50)
# 默认值参数
prt2(1, 3)
prt2(1, 3, 40)
prt2(1, 3, 40, 50)


def prt3(a, b, *c, **d):  # *：将多个参数收集到tuple中，**：多个参数收集到dict中
    print('a =', a, 'b =', b, 'c =', c, 'd =', d)


# 可变参数
prt3(1, 3, 4, 5, 40, name='lxy', age=22)


def prt4(*a, b, c, d):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d)


# 强制命名参数
prt4(1, 3, 4, b=-1, d=-2, c=-3)
