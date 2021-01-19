from turtle import Turtle, Screen
import turtle as t
import random

colours = ["teal", "blue", "salmon", "purple", "green", "gold", "royal blue", "gray", "black", "pink" ]

circle = Turtle()
number = [1, 2, 3]
t.colormode(255)
circle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for i in range(100):
    circle.circle(100)
    circle.color(random_color())
    circle.right(5)

screen = Screen()
screen.exitonclick()
