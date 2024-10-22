import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("50_states.csv")
state_df = pandas.DataFrame(states)
print(state_df)

state_answer = screen.textinput(title="Guess the state:", prompt="Enter the state name?").capitalize()
print(state_answer)

# for state in state_df.state:
#     if state_answer == state:
#         print("yes")
#     else:
#         print("no")






#code to get coords on click
# def mouse_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(mouse_coord)
#
# screen.mainloop()

screen.exitonclick()