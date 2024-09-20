from turtle import Turtle
import random as r

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.setheading(0)

    def move(self):
        self.forward(20)

    def change_heading(self):
        random_numb = r.randrange(-10,10)
        new_heading = 180 - random_numb
        self.setheading(self.heading()-new_heading)
        print(self.heading())