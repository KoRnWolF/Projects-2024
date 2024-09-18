from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snakey")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard.wall()
#main loop
game_run = True
while game_run:

    screen.update()
    time.sleep(0.1)
    snake.move()
    food_distance = snake.segments[0].distance(food)
    print(food_distance)
    #check food collision
    if food_distance < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()
    #check wall collision
    if snake.segments[0].xcor() >= 285 or snake.segments[0].xcor() <= -285:
        scoreboard.end_game()
        game_run = False
    if snake.segments[0].ycor() >= 285 or snake.segments[0].ycor() <= -285:
        scoreboard.end_game()
        game_run = False
    sliced = snake.segments[1:]
    #tail collision check
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) <= 0.1:
            game_run = False
            scoreboard.end_game()

screen.exitonclick()
