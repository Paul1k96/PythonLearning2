from turtle import *

hideturtle(), speed(0)


def move(x, y):
    penup(), goto(x, y), pendown()


def filling(angle, length, color, m=1):
    begin_fill(), fillcolor(color)
    for _ in range(4):
        lt(angle*m)
        fd(length)
    end_fill()


filling(120, 100, 'chocolate')
move(-15, -1), setheading(0)
filling(90, 70, 'SkyBlue', -1)

done()
