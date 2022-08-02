from turtle import *

hideturtle(), speed(0)


def filling(m=1, circ=False):
    begin_fill(), fillcolor('white')
    for _ in range(3):
        if circ:
            dot(30, 'black')
        lt(120*m)
        fd(100)
    end_fill()


filling()
penup(), goto(0, 60)
filling(-1, True)
filling(-1)

done()
