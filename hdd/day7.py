"""
    4字典：可变
    5集合：
"""


def ba_dict():
    fam_info = {'lxy': (25, 'male', 'stu'),
                'pjj': (26, 'female', 'tester'),
                'tdd': (3, 'female', 'dog')}
    # 通过键可以获取字典中对应的值
    print(fam_info['lxy'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in fam_info:
        print('{}\t--->\t{}'.format(elem, fam_info[elem]))
    # 更新字典中的元素
    fam_info['tdd'] = (3, 'female', 'eat and sleep')
    fam_info.update(lxy=(26, 'male', 'engineer'))
    print(fam_info)
    if 'tdd' in fam_info:
        print(fam_info['tdd'])
    print(fam_info.get('pjj'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(fam_info.get('lxy', ()))
    # 删除字典中的元素
    print(fam_info.popitem())
    print(fam_info.pop('???', 100))
    # 清空字典
    fam_info.clear()
    print(fam_info)


def ba_set():
    set1 = {2, 3, 4}
    print(set1)
    print('Length =', len(set1))  # 元素个数
    set2 = set(range(1, 3))
    print(set2)
    set1.add(1)
    print(set1)
    set2.update([4, 5])
    set2.discard(5)  # delete 5
    print(set2)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((2, 3, 4))
    print(set3.pop())
    print(set3)
    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set2 >= set3)
    # print(set1.issuperset(set2))


if __name__ == "__main__":
    ba_dict()
    ba_set()
