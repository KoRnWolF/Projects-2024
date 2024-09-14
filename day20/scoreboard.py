from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-20,280)
        self.color("white")
        self.write(arg = "Score:",align = "left", font=("Arial", 11, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg = f"Score:{self.score}",align = "left",font=("Arial", 11, "bold"))

    def end_game(self):
        """Rough code to end game"""
        print("You hit a something")
        print(f"GameOver, You score:{self.score}")
        exit()

    def wall(self):
        """Rough code to draw wall with a single turtle"""
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-280,280)
        self.pendown()
        self.goto(-280, -280)
        self.goto(280, -280)
        self.goto(280, 280)
        self.goto(-280, 280)



