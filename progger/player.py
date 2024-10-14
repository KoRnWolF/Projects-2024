from turtle import Turtle
from scoreboard import Scoreboard

POSITION = (0,-280)
MOVE_SPEED = 20
FINISH_LINE = 280
scoreboard = Scoreboard()
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

    def check_finish(self):
        self.goto(POSITION)
        scoreboard.level()

