import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
t = turtle.Turtle()
scorer = turtle.Turtle()

states = pandas.read_csv("50_states.csv")
state_df = pandas.DataFrame(states)
cont = True
score = 0
while cont:
    state_answer = screen.textinput(title="Guess the state:", prompt="Enter the state name?").capitalize()
    if state_answer == "exit":
        cont = False
    location = states[states.state == state_answer]
    if location.empty:
        t.hideturtle()
        t.penup()
        t.setposition(-200,0)
        t.write(f"Game Over - State not found!", font=("Arial", 20, "normal"))
        cont = False
    else:
        location_state = location.values[0][0]
        location_x = int(location.x)
        location_y = int(location.y)
        t.hideturtle()
        t.penup()
        t.speed("fastest")
        t.setposition(location_x, location_y)
        t.write(location_state)
        score += 1
        scorer.speed("fastest")
        scorer.clear()
        scorer.hideturtle()
        scorer.penup()
        scorer.setposition(-150, 340)
        scorer.write(f"Current score:{score}/50",font=("Arial", 20, "normal"))




# turtle.hideturtle()
# turtle.penup()
# turtle.setposition(row.x, row.y)
# turtle.write(states.state)

# for state in state_df.state:
#     if state_answer == state:
#         turtle.hideturtle()
#         turtle.penup()
#         # x = int(state_df.x)
#         # y = int(state_df.y)
#         # turtle.setposition(x, y)
#         turtle.write(state)






#code to get coords on click
# def mouse_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(mouse_coord)
#
# screen.mainloop()

screen.exitonclick()