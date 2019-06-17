from typing import Dict

names = ('l', 'xxx', 'yy yy', 'ppp j jj')
ages = (12, 13, 22, 43)
jobs = ('teacher', 'worker', 'engineer')
# zip并行迭代
for name, age, job in zip(names, ages, jobs):
    print('{0}--{1}--{2}'.format(name, age, job))
    print(name)

# 推导式创建序列
# list
a = [x * 2 for x in range(1, 6)]
print(a)

b = []
for x in range(1, 6):
    b.append(x * 2)
print(b)

cells = [(row, col) for row in range(1, 6, 2) for col in range(1, 8, 3)]
print(cells)

# dict推导式：统计字符串中每个字符出现的次数
my_text = 'i love you, i love pj, i love lxy,lpp jji x'
char_count = {c: my_text.count(c) for c in my_text}
print(char_count)

char_cnt = {}  # type: Dict[str, int]
for x in my_text:
    if x in char_cnt.keys():
        continue
    char_cnt.fromkeys(x)
    char_cnt[x] = my_text.count(x)
print(char_cnt)

# 集合推导式
u = {x for x in range(1, 100) if x % 9 == 0}
print(u)

# 生成器推导式
gnt = (x for x in range(4))
print(tuple(gnt))  # 生成器只能用一次

gnt = (x for x in range(4))
for x in gnt:
    print(x, end=',')
