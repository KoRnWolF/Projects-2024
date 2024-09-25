from turtle import Turtle
import random
CAR_SPEED = 8

class CarManager:
    def __init__(self):
        self.cars = []
        self.add_car()

    def add_car(self):
        y_start = random.randrange(-250, 260)
        x_start = random.randrange(300, 500)
        car = Turtle("square")
        car.penup()
        car.color("black")
        car.shape("square")
        car.shapesize(1, 2)
        car.setheading(180)
        car.goto(x_start, y_start)
        self.cars.append(car)


    def car_move(self):
        for car in self.cars:
            car.forward(CAR_SPEED)
            if car.xcor() <= -300:
                car.hideturtle()
                self.cars.remove(car)


