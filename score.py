from turtle import Turtle
ALIGMENT = "center"
FONT = ("Verdana", 17, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()
        self.speed("fastest")

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def up_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)