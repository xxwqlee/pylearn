"""
    1字符串:不可变
"""
import time


def ba_str():
    str1 = 'hello, world!'
    # 通过len函数计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!
    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('？？？'))  # -1
    # 与find类似但找不到子串时会引发异常
    print(str1.index('or'))  # 8
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧指定字符的拷贝
    print(str3.strip(' jm'))
    #  join操作
    l1 = ['a', 'b', 'c']
    str4 = ' '.join(l1)
    print(str4)


def test_str():
    x = 1000000
    # 方法一
    start_time1 = time.time()
    s1 = ''
    for n in range(x):
        s1 += str(n)
    end_time1 = time.time()
    print(end_time1 - start_time1)
    # 方法二
    start_time2 = time.time()
    list1 = []
    for n in range(x):
        list1.append(str(n))
    s2 = ''.join(list1)
    end_time2 = time.time()
    print(end_time2 - start_time2)
    # 方法3
    start_time3 = time.time()
    s3 = ''.join(map(str, range(x)))
    end_time3 = time.time()
    print(end_time3 - start_time3)


if __name__ == "__main__":
    ba_str()
    test_str()
