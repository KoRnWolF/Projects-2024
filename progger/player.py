from turtle import Turtle
POSITION = (0,-280)
MOVE_SPEED = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.goto(POSITION)


    def player_move(self):
        new_y = self.ycor() + MOVE_SPEED
        self.goto(self.xcor(), new_y)



