"""
    2列表：可变
    3元组：不可变
"""
import sys


def ba_list():
    fruits1 = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits1 += ['pitaya', 'pear', 'mango']
    print('fruit1 is ', fruits1)
    # 循环遍历列表元素
    for fruit in fruits1:
        print(fruit.title(), end='\t')
        print(fruit)
    # 列表切片
    fruits2 = fruits1[1:4]
    print('fruit2 is ', fruits2)
    # fruits3 = fruits1  # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits1[:]
    print('fruit3 is ', fruits3)
    fruits4 = fruits1[-3:-1]
    print('fruit4 is ', fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits1[::-1]
    print('fruit5 is ', fruits5)
    # 列表排序
    list1 = ['orange', 'apple', 'zoo',
             'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)  # 原始列表
    print(list2)  # 首字母顺序
    print(list3)  # 首字母顺序反向
    print(list4)  # 字符长度
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)
    ge = [x + y for x in 'ABC' for y in '12345']
    print(ge)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    gnt = [x ** 2 for x in range(1, 10)]
    print(sys.getsizeof(gnt))  # 查看对象占用内存的字节数
    print(gnt)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    gnt_obj = (x ** 2 for x in range(1, 10))
    print(sys.getsizeof(gnt_obj))  # 相比生成式生成器不占用存储数据的空间
    print(gnt_obj)
    for val in gnt_obj:
        print(val)
    # 生成器对象只能用一次
    gnt1 = list(gnt_obj)
    print(gnt1)


def ba_tup():
    # 定义元组
    t = ('lxy', 20, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 40, True, '云南昆明')
    print(t)
    # 将元组转换成列表
    print(list(t))
    # 将列表转换成元组
    print(tuple(list(t)))


if __name__ == "__main__":
    ba_list()
    print("*" * 50)
    ba_tup()
