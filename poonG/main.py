import turtle
import time
from player import Player
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

player_1 = Player((-350, 0))
player_2 = Player((350, 0))
ball = Ball()
score_p1 = Scoreboard((-350,280))
score_p2 = Scoreboard((320,280))

screen.listen()
screen.onkey(player_1.up_player_1,"Up")
screen.onkey(player_1.down_player_1,"Down")

screen.onkey(player_2.up_player_2,"w")
screen.onkey(player_2.down_player_2,"s")

go = True
while go:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.xcor() <= -325 and player_1.distance(ball) <= 50:
        ball.bounce_paddle()

    if ball.xcor() >= 325 and player_2.distance(ball) <= 50:
        ball.bounce_paddle()

    #check for ball wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #check for score and reset ball
    if ball.xcor() > 360:
        score_p1.increase_p1()
        ball.reset_ball()

    if ball.xcor() < -360:
        score_p2.increase_p2()
        ball.reset_ball()

screen.exitonclick()



