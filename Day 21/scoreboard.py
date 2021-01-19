from turtle import Turtle
from snake import Snake
from food import Food
import time

SCORE = 0


class Scoreboard(Turtle, Snake):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 26, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()