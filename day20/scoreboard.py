from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.hideturtle()
        self.goto(-60,280)
        self.color("white")
        self.write(arg = f"Score: 0 High Score:{self.high_score}",align = "left", font=("Arial", 11, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 280)
        self.color("white")
        self.write(arg = f"Score:{self.score} High Score:{self.high_score}",align = "left",font=("Arial", 11, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
        self.update_scoreboard()



