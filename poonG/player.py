from turtle import Turtle

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.resizemode("user")
        self.shapesize(5, 1)
    def up_player_1(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_player_1(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up_player_2(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_player_2(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)