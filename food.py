from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.setpos(randint(-280, 280), randint(-280, 280))

    def generate_food(self):
        self.setpos(randint(-280, 280), randint(-280, 280))
