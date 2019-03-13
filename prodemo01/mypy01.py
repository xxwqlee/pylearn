print('hello pycharm')
a = int(input('请输入一个数字：'))

if a < 20:
    print(a)

if 3 < a and a is not 10:
    print('a=', a)

x = int(input("请输入 x 坐标"))
y = int(input("请输入 y 坐标"))
if x == 0 and y == 0:
    print("原点")
elif x == 0:
    print("y 轴")
elif y == 0:
    print("x 轴")
elif x > 0 and y > 0:
    print("第一象限")
elif x < 0 < y:
    print("第二象限")
elif x < 0 and y < 0:
    print("第三象限")
else:
    print("第四象限")
