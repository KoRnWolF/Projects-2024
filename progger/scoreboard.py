from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 285)
        self.score = 0
        self.write(arg= f"Score:{self.score}", align = "left", font=("Arial", 11, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg= f"Score:{self.score}", align = "left", font=("Arial", 11, "bold"))


