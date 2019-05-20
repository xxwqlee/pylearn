"""
    练习：
    1.水仙花数
    2.完美数
    3.百钱百鸡
    4.斐波那契数列
"""


def nar_num():
    for x in range(100, 1000):
        if (x % 100 % 10) ** 3 + int(x % 100 / 10) ** 3 + int(x / 100) ** 3 == x:
            print('%d is a narnum' % x)


def pft_num(n):
    for x in range(1, n):
        z = 0
        for y in range(1, x):
            if x % y == 0:
                z += y
        if z == x:
            print("%d is a perfect number" % x)


def chicken_num():
    for x in range(20):
        for y in range(int((100 - 5 * x) / 3)):
            if 14 * x + 8 * y == 200:
                print("male %d female %d young %d" % (x, y, 100 - x - y))


def fib_num(n):
    a, b = 1, 1
    while a < n:
        print(a, end='\t')
        a, b = b, a + b


if __name__ == '__main__':
    nar_num()  # 打印所有的三位水仙花数
    pft_num(1000)  # 10000以内的所有完美数
    chicken_num()
    fib_num(100)  # 100 以内的斐波那契数列

