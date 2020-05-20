import random
import turtle
tut = turtle.Pen()
da = random.randint(1,2)
if da == 1:
    tut.right(90)
    tut.forward(50)
    tut.backward(25)
    tut.left(90)
    tut.forward(20)
    tut.right(90)
    tut.forward(25)
    tut.backward(50)
elif da == 2:
    tut.forward(50)
    tut.backward(25)
    tut.right(90)
    tut.forward(100)
