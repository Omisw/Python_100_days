from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" {self.left_score} | {self.right_score}", align="center", font=("Courier", 20, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()


