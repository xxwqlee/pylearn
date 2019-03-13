import turtle
# 画棋盘18*18

p = turtle.Pen()
my_colors = ('red', 'green', 'blue')
p.speed(0.1)
for x in range(-90, 91, 10):
    p.penup()
    p.goto(x, 90)
    p.pendown()
    p.color(my_colors[abs(x) % len(my_colors)])
    p.goto(x, -90)
for x in range(-90, 91, 10):
    p.penup()
    p.goto(-90, x)
    p.pendown()
    p.color(my_colors[abs(x) % len(my_colors)])
    p.goto(90, x)
turtle.done()
