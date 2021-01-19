from turtle import Turtle, Screen
import turtle as t
import random

colours = ["teal", "blue", "salmon", "purple", "green", "gold", "royal blue", "gray", "black", "pink" ]

line = Turtle()
line.pensize(10)
number = [1, 2, 3]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for i in range(500):
    random_number = random.choice(number)
    line.color(random_color())
    line.forward(25)
    if random_number == 1:
        line.left(90)
    elif random_number == 2:
        line.right(90)
    elif random_number == 3:
        line.backward(25)

screen = Screen()
screen.exitonclick()