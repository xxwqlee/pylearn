"""
    1.字典的遍历：values():值，items()：键值对
    2. enumerate() 同时返回元素及其索引
    3.practise: 给定下面两个列表 attributes 和 values，要求
    针对 values 中每一组子列表 value，输出其和attributes 中
    的键对应后的字典，最后返回字典组成的列表
"""


def my_circle():
    fam_info = {'lxy': (25, 'male', 'stu'),
                'pjj': (26, 'female', 'tester'),
                'tdd': (3, 'female', 'dog')}
    for keys in fam_info:
        print(f'keys: {keys}')
    for items in fam_info.items():
        print(f'items: {items }')
    for values in fam_info.values():
        print(f'values: {values }')
    for index, elem in enumerate(fam_info.items()):
        print(f'index{index}\telement:{elem}')


def practise():
    attributes = ['name', 'dob', 'gender']
    values = [['jason', '2000-01-01', 'male'],
              ['mike', '1999-02-02', 'male'],
              ['nancy', '1998-03-03', 'female']
              ]
    print([dict(zip(attributes, val))for val in values])
    lis = []
    for value in values:
        dic = {}
        for i in range(len(attributes)):
            dic[attributes[i]] = value[i]
        lis.append(dic)
    print(lis)


if __name__ == '__main__':
    my_circle()
    practise()
