import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()


screen.bgcolor("midnight blue")
screen.title("Snake Game Part1")
screen.tracer(0)
screen.setup(height=600, width=600)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
# is_start = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 30:
        scoreboard.update_score()
        food.relocate()
        snake.extend()
    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect tail collision
    for snake_bit in snake.snake_bits[1:]:
        if snake.head.distance(snake_bit) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
