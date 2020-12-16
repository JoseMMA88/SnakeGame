from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        self.body_count = 3
        self.position = {"x": 0, "y": 0}
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        # Snake Setup
        for i in range(self.body_count):
            self.add_body(self.position)

    def reset(self):
        for body in self.snake:
            body.goto(2000, 2000)

        self.snake.clear()
        self.body_count = 3
        self.position = {"x": 0, "y": 0}
        self.create_snake()
        self.head = self.snake[0]

    def add_body(self, position):
        body = Turtle("square")
        body.penup()
        body.color("white")
        body.goto(position["x"], position["y"])
        self.position["x"] -= 20
        self.position["y"] = position["y"]
        self.snake.append(body)

    def grown(self):
        self.body_count += 1
        position = {"x": self.snake[-1].xcor(), "y": self.snake[-1].ycor()}
        self.add_body(position)

    def move(self):
        # Snake Movement
        for i in range(len(self.snake) - 1, 0, -1):
            if i - 1 >= 0:
                self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.head.forward(20)

    def head_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def head_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def head_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def head_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


