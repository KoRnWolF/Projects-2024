import random
import turtle
from turtle import Turtle, Screen

frik = Turtle()
james = Turtle()
tim = Turtle()

# for _ in range(0,4):
#     frik.forward(100)
#     frik.left(90)

# for x in range(0, 15):
#     frik.forward(10)
#     frik.penup()
#     frik.forward(10)
#     frik.pendown()

# def shape(sides):
#     for _ in range(sides):
#         frik.forward(100)
#         frik.right(360/sides)
#
# for shape_side in range(3,10):
#     shape(shape_side)
#     frik.color(random.choice(colors))
frik.width(10)
james.width(10)
tim.width(10)
turtle.colormode(255)
turtle.screensize(200,200)
def rand_color():
    r = random.randrange(0, 256, 100)
    b = random.randrange(0, 256)
    g = random.randrange(0, 256)
    my_tuple = (r, b, g)
    return my_tuple

frik.speed("fastest")
james.speed("fastest")
tim.speed("fastest")
direction = [0, 90, 180, 270]
go = True
while go:

    frik.setheading(random.choice(direction))
    frik.forward(20)
    frik.pencolor(rand_color())

    james.setheading(random.choice(direction))
    james.forward(20)
    james.pencolor(rand_color())

    tim.setheading(random.choice(direction))
    tim.forward(20)
    tim.pencolor(rand_color())


# frik.hideturtle()
# frik.speed("fastest")
# def draw_circle(head_deg):
#
#     for _ in range(int(360 / head_deg)):
#         frik.circle(100)
#         frik.pencolor(rand_color())
#         frik.setheading(frik.heading() + head_deg)
#
# draw_circle(5)

screen = Screen()
screen.exitonclick()

