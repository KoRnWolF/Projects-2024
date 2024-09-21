import turtle
import time
from player import Player
from ball import Ball

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

player_1 = Player((-350, 0))
player_2 = Player((350, 0))
ball = Ball()

screen.listen()
screen.onkey(player_1.up_player_1,"Up")
screen.onkey(player_1.down_player_1,"Down")

screen.onkey(player_2.up_player_2,"w")
screen.onkey(player_2.down_player_2,"s")

go = True
while go:

    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.xcor() <= -340 and player_1.distance(ball) <= 50:
        ball.bounce_paddle()

    if ball.xcor() >= 340 and player_2.distance(ball) <= 50:
        ball.bounce_paddle()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()
#TODO setup boundries
#TODO Setup scoreboard


