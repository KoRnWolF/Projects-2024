import turtle
import time
from player import Player
from ball import Ball

screen = turtle.Screen()
screen.screensize(600,600)
screen.tracer(0)

player = Player()
ball = Ball()

screen.listen()
screen.onkey(player.up_player_1,"Up")
screen.onkey(player.down_player_1,"Down")

screen.onkey(player.up_player_2,"w")
screen.onkey(player.down_player_2,"s")

go = True
while go:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if player.players[0].distance(ball) <= 30:

        ball.change_heading()

    if player.players[1].distance(ball) <= 30:
        ball.change_heading()


screen.exitonclick()
#TODO Ball bouncing incorrectly
#TODO setup boundries
#TODO Setup scoreboard


