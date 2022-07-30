from turtle import *
from random import randrange

# settings and colors
Screen().bgcolor('SkyBlue'), speed(0), hideturtle(), pensize(2)
colormode(255)  # for Python 3


def move(x, y):
    penup(), goto(x, y), pendown()


def snowflake(size, x=0, y=0):
    pencolor(randrange(256), randrange(256), randrange(256))
    size_for_branch = size / 4
    angle = 0
    move(x, y), setheading(0)  # move to snowflake center and reset angle to default

    for _ in range(8): # snowflake
        for _ in range(4):  # big branches
            setheading(angle), fd(size_for_branch)
            x_tmp, y_tmp = pos()

            for n in (1, -1):  # little branches
                setheading(45*n + angle), fd(size_for_branch), move(x_tmp, y_tmp)

            setheading(angle)

        angle += 45
        move(x, y)


snowflake(30)
cord = (-100, 100, 100, -100, -100)
for i in range(4):
    snowflake(randrange(10, 70), cord[i], cord[i+1])

done()  # stop-command in IDE(turtle module)
