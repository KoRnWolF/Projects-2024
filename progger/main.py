from turtle import Turtle, Screen
import time
from player import Player
from car_manager_backup import CarManager
from scoreboard import ScoreBoard

screen = Screen()
car_speed = 8
scoreboard = ScoreBoard()

screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("white")

car_amount = 30

player = Player()

car_manager_backup = CarManager()

screen.listen()
screen.onkeypress(player.player_move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager_backup.car_move(car_speed)
    if len(car_manager_backup.cars) < 20:
        car_manager_backup.add_car()

    if player.ycor() >= 280:
        player.goto(0,-280)
        car_speed = car_speed + 1
        scoreboard.increase_score()




screen.exitonclick()