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
all_states = states.state.to_list()

cont = True
score = 0
answers = []
while cont:
    state_answer = screen.textinput(title=f"Guess the state: {score}/50", prompt="Enter the state name?").title()
    print(state_answer)
    location = states[states.state == state_answer]
    if len(answers) == 50:
        t.hideturtle()
        t.penup()
        t.setposition(-200,0)
        t.write(f"Congrats You Win!", font=("Arial", 20, "normal"))
        cont = False
    ###section if you would like to end game on wrong answer
    # if location.empty:
        # t.hideturtle()
        # t.penup()
        # t.setposition(-200,0)
        # t.write(f"Game Over - State not found!", font=("Arial", 20, "normal"))
        # cont = False
        # print("Wrong")
        #
        # pass

    if state_answer == "Exit":
        break

    else:
        if state_answer not in answers:
            location_state = location.values[0][0]
            location_x = int(location.x)
            location_y = int(location.y)
            t.hideturtle()
            t.penup()
            t.speed("fastest")
            t.setposition(location_x, location_y)
            t.write(location_state)

            score += 1
            answers.append(state_answer)
            
            scorer.speed("fastest")
            scorer.clear()
            scorer.hideturtle()
            scorer.penup()
            scorer.setposition(-150, 340)
            scorer.write(f"Current score:{score}/50",font=("Arial", 20, "normal"))
            all_states.remove(state_answer)

df = pandas.DataFrame(all_states, columns=["Missed States"])
df.to_csv("states_to_learn.csv", index=False)

#code to get coords on click
# def mouse_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(mouse_coord)
#
# screen.mainloop()
