import turtle as t
from turtle import Screen
import random

colors = ["red", "blue", "green", "purple", "orange"]
ylocation = 40, -40, 80, -80, 0
turts = []
screen =Screen()
usr_bet = screen.textinput("Take Bets", "Place your bet on who will win(red/blue/green/purple/orange):")

for turt in range(0,5):

    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(-430, ylocation[turt])
    new_turtle.color(colors[turt])
    turts.append(new_turtle)


line = t.Turtle()
line.penup()
line.goto(430,-100)
line.pendown()
line.goto(430, 100)
line.hideturtle()
run = True
min_speed = 2
max_speed = 7.9

while run:
    for turt in turts:
        if turt.xcor() > 407:
            run = False
            winner = turt.pencolor()
        turt.forward(random.uniform(min_speed,max_speed))

if usr_bet == winner:
    print(f"The winner is {winner},You win!")
else:
    print(F"The winner is {winner},You lose!")













t.exitonclick()


