# lambda表达式, 匿名函数

g = [lambda a:a*2, lambda b:b*3]

print(g[0](3), g[1](3))

# eval()函数

eval("print('dad')")

x = 10
y = 20
c = eval('x+y')
print(c)

dict1 = dict(x=100, y=200)
print(dict1)

d = eval('x+y', dict1)
print(d)
