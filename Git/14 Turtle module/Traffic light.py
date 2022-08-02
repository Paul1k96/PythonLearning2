from turtle import *

hideturtle(), speed(0)


def filling(length, col='black', circ=False):
    begin_fill(), fillcolor(col)
    angle = 90
    if not circ:
        for _ in range(2):
            lt(angle)
            fd(length*2)
            lt(angle)
            fd(length)
    else:
        circle(length)
    end_fill()


filling(100)
n = 15
penup()
for i in ('green', 'yellow', 'red'):
    goto(-50, n)
    filling(25, i, True)
    n += 60

done()
