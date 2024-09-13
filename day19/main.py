import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
usr_bet = screen.textinput("Take Bets", "Place your bet on who will win(red/blue/green/purple/orange):")

draw_line = Turtle()
draw_line.hideturtle()
draw_line.penup()
draw_line.setpos(220,-100)
draw_line.setheading(90)
draw_line.pendown()
draw_line.setpos(220,100)

def ini_turtle(turt):
    t_color = ""
    t_posx = 0
    t_posy = 0

    if turt == tim:
        t_color = "red"
        t_posx = -225
        t_posy = 0

    if turt == tom:
        t_color = "blue"
        t_posx = -225
        t_posy = 40

    if turt == top:
        t_color = "green"
        t_posx = -225
        t_posy = 80

    if turt == tol:
        t_color = "purple"
        t_posx = -225
        t_posy = -40

    if turt == tix:
        t_color = "orange"
        t_posx = -225
        t_posy = -80

    turt.color(t_color)
    turt.speed("slow")
    turt.penup()
    turt.setpos(t_posx, t_posy)
    turt.shape("turtle")

tim = Turtle()
tom = Turtle()
top = Turtle()
tol = Turtle()
tix = Turtle()

ini_turtle(tim)
ini_turtle(tom)
ini_turtle(top)
ini_turtle(tol)
ini_turtle(tix)

move = True
min_speed = 0.1
max_speed = 5.0

while move:
    pos_tim = tim.xcor()
    pos_tom = tom.xcor()
    pos_top = top.xcor()
    pos_tol = tol.xcor()
    pos_tix = tix.xcor()

    if pos_tim > 200:
        move = False
        color = "red"
    tim.forward(random.uniform(min_speed,max_speed))

    if pos_tom > 200:
        move = False
        color = "blue"
    tom.forward(random.uniform(min_speed,max_speed))

    if pos_top > 200:
        move = False
        color = "green"
    top.forward(random.uniform(min_speed,max_speed))

    if pos_tol > 200:
        move = False
        color = "purple"
    tol.forward(random.uniform(min_speed,max_speed))

    if pos_tix > 200:
        move = False
        color = "orange"
    tix.forward(random.uniform(min_speed,max_speed))
print(f"You selected {usr_bet}.")
if usr_bet == color:
    print(f"{color} won, you Win!")
else:
    print(f"{color} won, you Lost!")

screen.exitonclick()

