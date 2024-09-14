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
    tail_distance = snake.segments[0].distance(snake.segments[2])
    print(food_distance)

    if food_distance < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.add_segments()
    #Rough code to wall check
    if snake.segments[0].xcor() > 279 or snake.segments[0].xcor() < -279:
        scoreboard.end_game()
    if snake.segments[0].ycor() > 279 or snake.segments[0].ycor() < -279:
        scoreboard.end_game()
    #Rough code to tail check
    if tail_distance <= 0.1:
        scoreboard.end_game()

screen.exitonclick()
