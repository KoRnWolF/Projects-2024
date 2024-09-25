from turtle import Turtle, Screen
import time
from player import Player
from car_manager_backup import CarManager


screen = Screen()

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

    car_manager_backup.car_move()
    if len(car_manager_backup.cars) < 20:
        car_manager_backup.add_car()

    player.check_finish()



screen.exitonclick()