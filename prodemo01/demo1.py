import turtle
import time

x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100


turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)

time01 = time.time()

a = ''
for i in range(10000000):
    a += 'lxy'
time02 = time.time()

print('time=' + str(time02-time01))
time03 = time.time()
li = []
for i in range(10000000):
    li.append('lxy')

a = ''.join(li)
time04 = time.time()

print('time='+str(time04-time03))
