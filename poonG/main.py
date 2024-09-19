import turtle
from turtle import Turtle
import time

STARTING_LOC = [(-450, 20), (-450, 0), (-450,-20)]
player_1 = []

screen = turtle.Screen()
screen.screensize(600,600)
screen.tracer(0)
screen.listen()


for position in STARTING_LOC:

    new_segment = Turtle("square")
    new_segment.speed("fastest")
    new_segment.penup()
    new_segment.goto(position)
    new_segment.setheading(90)
    player_1.append(new_segment)

go = True
while go:
    screen.update()
    time.sleep(0.1)
    for seg_idx in range(len(player_1) - 1, 0, -1):
        new_x = player_1[seg_idx - 1].xcor()
        new_y = player_1[seg_idx - 1].ycor()
        player_1[seg_idx].goto(new_x, new_y)
    player_1[0].forward(20)










screen.exitonclick()


