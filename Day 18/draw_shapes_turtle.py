from turtle import Turtle, Screen
import random

juanito = Turtle()
colours = ["teal", "blue", "salmon", "purple", "green", "gold", "royal blue", "gray", "black", "pink" ]
juanito.shape("turtle")

juanito.resizemode()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        juanito.forward(100)
        juanito.right(angle)

for num_side_n in range(3, 11):
    juanito.color(random.choice(colours))
    draw_shape(num_side_n)

screen = Screen()
screen.exitonclick()