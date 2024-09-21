import turtle
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.players = []
        self.starting_loc = [(-350, 0), (350, 0)]
        self.create_player()

    def create_player(self):
        for position in self.starting_loc:
            player = Turtle("square")
            player.color("white")
            player.speed("fastest")
            player.penup()
            player.goto(position)
            player.resizemode("user")
            player.shapesize(5,1)
            self.players.append(player)

    def up_player_1(self):
        new_y = self.players[0].ycor() + 20
        self.players[0].goto(self.players[0].xcor(), new_y)

    def down_player_1(self):
        new_y = self.players[0].ycor() - 20
        self.players[0].goto(self.players[0].xcor(), new_y)

    def up_player_2(self):
        new_y = self.players[1].ycor() + 20
        self.players[1].goto(self.players[1].xcor(), new_y)

    def down_player_2(self):
        new_y = self.players[1].ycor() - 20
        self.players[1].goto(self.players[1].xcor(), new_y)