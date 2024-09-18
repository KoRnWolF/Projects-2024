from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):

        super().__init__()
        self.color("green")
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.goto(float((random.randrange(-260, 260))), float((random.randrange(-260, 260))))





