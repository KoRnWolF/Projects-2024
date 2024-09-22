from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()

        self.score_p1 = 0
        self.score_p2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(arg= "Score:", align = "left", font=("Arial", 11, "bold"))

    def increase_p1(self):
        self.score_p1 += 1
        self.clear()
        self.write(arg= f"Score:{self.score_p1}", align = "left", font=("Arial", 11, "bold"))

    def increase_p2(self):
        self.score_p2 += 1
        self.clear()
        self.write(arg= f"Score:{self.score_p2}", align = "left", font=("Arial", 11, "bold"))

