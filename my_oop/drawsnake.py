import turtle


def draw_snake(rad, angle, len, neck_rad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neck_rad+1, 180)
    turtle.fd(rad*2/3)


def main():
    turtle.setup(1000, 800, 0, 0)
    python_size = 30
    turtle.pensize(python_size)
    turtle.pencolor('blue')
    turtle.seth(-40)
    draw_snake(40, 80, 3, python_size/2)
    turtle.done()


main()
