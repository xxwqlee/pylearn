d = {'name': 'l', 'age': 10, 'job': 'cs'}

for x in d.items():
    print(x)

# 0-100求和
print(sum(range(101)))
print(sum(range(0, 101, 2)))
print(sum(range(1, 100, 2)))

# 打印九九乘法表
for m in range(1, 10):
    for n in range(1, m + 1):
        print('{0} * {1} = {2}'.format(m, n, (m * n)), end='\t')
    print()
