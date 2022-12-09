from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = []
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.left, "Left")



snake_game = True
while snake_game:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    # detect collision with food.
    if my_snake.head.distance(food) < 13:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

#     detect collision with wall.
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        scoreboard.reset()
        my_snake.reset()


#     detect collision with tail.
    for segment in my_snake.snake[1:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.reset()
            my_snake.reset()


screen.exitonclick()
