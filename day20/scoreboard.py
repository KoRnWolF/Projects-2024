from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()
        self.goto(-60,280)
        self.color("white")
        self.write(arg = "Score:",align = "left", font=("Arial", 11, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(-60, 280)
        self.color("white")
        self.write(arg = f"Score:{self.score}",align = "left",font=("Arial", 11, "bold"))

    def end_game(self):
        """Method to end game"""
        print("You hit a something")
        print(f"GameOver, You score:{self.score}")
        self.goto(-60, 0)
        self.write(arg = f"GAME OVER",align = "left",font=("Arial", 11, "bold"))



