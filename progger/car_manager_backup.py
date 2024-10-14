import turtle
from turtle import Turtle
import random


color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90),
              (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166),
              (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159),
              (175, 200, 188), (34, 151, 210), (65, 66, 56)]

CAR_MOVE_INC = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.add_car()
        self.car_speed = 8

    def add_car(self):
        y_start = random.randrange(-250, 260)
        x_start = random.randrange(300, 500)
        turtle.colormode(255)
        car = Turtle("square")
        car.penup()
        car.color(random.choice(color_list))
        car.shape("square")
        car.shapesize(1, 2)
        car.setheading(180)
        car.goto(x_start, y_start)
        self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() <= -300:
                car.hideturtle()
                self.cars.remove(car)

    def level_up(self):
        self.car_speed += CAR_MOVE_INC
        print(self.car_speed)

