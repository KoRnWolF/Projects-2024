import random
import turtle
#import colorgram
from turtle import Turtle
# color_list = []
# colors = colorgram.extract("spotty.jpg",30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_tuple = (red, green, blue)
#     color_list.append(color_tuple)

color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90),
              (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166),
              (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159),
              (175, 200, 188), (34, 151, 210), (65, 66, 56)]

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
tim.penup()
x = -430
y = -350
tim.setpos(x,y)
tim.pendown()
tim.hideturtle()
#changable parameters
dot_space = 40
row_amt = 19
column_amt = 22
dot_size = 20
def draw_dots():

    for _ in range(0, column_amt):

        tim.dot(dot_size, random.choice(color_list))
        tim.penup()
        tim.forward(dot_space)
        tim.pendown()
def set_pos(y_ax):

    tim.penup()
    tim.setpos(x, y_ax)
    tim.pendown()

for _ in range(row_amt):
    increase = dot_space
    y += increase
    draw_dots()
    set_pos(y)

tim.getscreen()
turtle.exitonclick()