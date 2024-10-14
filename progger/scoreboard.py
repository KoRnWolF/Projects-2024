from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.increase = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-280,280)

    def game_over_check(self):
        self.goto(0, 0)
        self.write(arg= f"GAME OVER", align = "left", font=("Arial", 11, "bold"))

    def level(self):
        self.current_level += 1
        self.clear()
        self.write(arg= f"Level:{self.current_level}", align = "left", font=("Arial", 11, "bold"))


