# Day 19 - Fisrt exercise.

from turtle import Turtle, Screen

line = Turtle()
screen = Screen()

def move():
    line.forward(10)

def back():
    line.backward(10)

def left():
    line.left(10)

def right():
    line.right(10)

def reset():
    line.reset()


screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()