# 测试递归函数的基本原理


def recursion1(n):
    print(n)
    if not n:
        print('over')
    else:
        recursion1(n-1)


def recursion2(n):
    print(n)
    if not n:
        print('over')
    else:
        recursion2(n-1)
    print('***', n)


recursion1(4)
print('*******************')
recursion2(4)

# 递归算阶乘


def factorial(n):
    if 1 == n:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
