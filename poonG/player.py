import turtle
from turtle import Turtle

class Player:

    def __init__(self):
        self.players = []
        self.starting_loc = [(-450, 0), (450, 0)]
        self.create_player()

    def create_player(self):
        for position in self.starting_loc:
            player = Turtle("square")
            player.speed("fastest")
            player.penup()
            player.goto(position)
            player.setheading(90)
            player.resizemode("user")
            player.shapesize(1,5,1)
            self.players.append(player)

    def up_player_1(self):
        self.players[0].forward(20)

    def down_player_1(self):
        self.players[0].backward(20)

    def up_player_2(self):
        self.players[1].forward(20)

    def down_player_2(self):
            self.players[1].backward(20)