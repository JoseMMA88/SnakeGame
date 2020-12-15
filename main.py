from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
# Turn off the tracer to prevent blinking
screen.tracer(0)


# Snake Setup
snake = Snake()

# Food Setup
food = Food()

# Score Setup
score = Score()

# Listen Keys
screen.listen()
screen.onkeypress(key="Up", fun=snake.head_up)
screen.onkeypress(key="Down", fun=snake.head_down)
screen.onkeypress(key="Left", fun=snake.head_left)
screen.onkeypress(key="Right", fun=snake.head_right)

# GAME MAINLOOP
is_game = True
while is_game:
    # Refresh the screen to prevent blinking at moving the snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check collisions with food
    if snake.head.distance(food) < 15:
        food.generate_food()
        score.up_score()
        snake.grown()

    # Check collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        is_game = False

    # Check collision with snake own tail
    for body in snake.snake[1:]:
        if snake.head.distance(body) < 10:
            score.game_over()
            is_game = False


screen.exitonclick()