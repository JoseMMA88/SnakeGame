from turtle import Turtle


ALIGMENT = "center"
FONT = ("Verdana", 17, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            h_score = int(file.read())

        self.score = 0
        self.high_score = h_score

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()
        self.speed("fastest")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def up_score(self):
        self.score += 1
        self.update_scoreboard()

    def start(self):
        self.home()
        self.write(f"PRESS 'SPACE' TO START", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("high_score.txt") as file:
                h_score = int(file.read())
                if self.high_score > h_score:
                    with open("high_score.txt", "w") as file1:
                        file1.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()