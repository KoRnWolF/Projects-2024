from turtle import Turtle, Screen
import time
from player import Player
from car_manager_backup import CarManager
from scoreboard import Scoreboard

screen = Screen()
car_speed = 8
scoreboard = Scoreboard()

screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
car_manager_backup = CarManager()

screen.listen()
screen.onkeypress(player.player_move, "Up")


x = 0
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager_backup.car_move()

    if x == 6:
        car_manager_backup.add_car()
        x = 0
    x += 1

    for car in car_manager_backup.cars:
        if car.distance(player) < 15:
            game_on = False
            scoreboard.game_over_check()

    if player.ycor() >= 280:
        player.check_finish()
        car_manager_backup.level_up()

screen.exitonclick()