from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)
def move_back():
    tim.back(10)
def head_left():
    current_head = tim.heading()
    tim.setheading(current_head + 10)
def head_right():
    current_head = tim.heading()
    tim.setheading(current_head - 10)
def reset():
    tim.reset()
def undo():
    tim.undo()
def pen():
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()

screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(head_left, "Left")
screen.onkey(head_right, "Right")
screen.onkey(move_back, "Down")
screen.onkey(reset, "c")
screen.onkey(undo, "x")
screen.onkey(pen, "z")
screen.exitonclick()

