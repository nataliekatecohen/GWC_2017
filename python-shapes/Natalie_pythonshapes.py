from turtle import *
import math

t = Turtle()

t.up()

# set start position
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

while True:
    try:
        sides = int(input("How many sides will there be in your shape?"))
        break
    except ValueError:
        print("Error")
        continue
        break
    if sides<=2:
        print("Error")
        continue
        break

angle = 360/sides
size = int(input("How large would you like your shape to be?"))
color = input("What color would you like your outline to be?")

t.down()

# making the shape
for turns in range(sides):
    t.forward(size)
    t.left(angle)
    t.pencolor(color)

exitonclick()
