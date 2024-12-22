from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
sb = Scoreboard()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
sb.reset()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()

        sb.increase_score()
        snake.extend()

    if snake.segments[0].xcor()>295 or snake.segments[0].xcor()<-295 or snake.segments[0].ycor()>295 or snake.segments[0].ycor()<-295:
        sb.reset()
        snake.reset()


    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg)<10:
            sb.reset()
            snake.reset()

screen.exitonclick()
