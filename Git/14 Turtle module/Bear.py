from turtle import *

Screen().setup(400, 500), speed(0), hideturtle()


def move(x, y):
    penup(), goto(x, y), pendown()


def eyes(x=1):
    pensize(12), move(55 * x, 40), dot(), pensize(1)


def ears(x=1):
    move(100 * x, 160), circle(40)


# nose
circle(10), goto(0, -80)

# mouth and face
move(0, -110), circle(75), circle(150)

# nose and eyes
for i in (-1, 1):  # -1 and 1 x-mirror
    eyes(i)
    ears(i)

done()  # stop-command in IDE(turtle module)
