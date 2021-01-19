# Day 18 - Final challenge "Art painting"


from turtle import Turtle, Screen
import turtle as t
import random

color_list = [(238, 235, 229), (244, 246, 249), (205, 154, 100), (230, 242, 236), (68, 83, 123), (146, 64, 83), (244, 233, 237), (227, 218, 106), (112, 91, 77), (215, 129, 162), (48, 120, 88), (206, 90, 117), (127, 171, 193), (218, 78, 71), (133, 194, 131), (35, 164, 176), (57, 173, 158), (59, 48, 62), (78, 109, 189), (86, 53, 78), (58, 58, 64), (88, 53, 49), (57, 59, 95), (175, 188, 57), (160, 212, 122), (3, 121, 99), (223, 171, 182), (229, 174, 162), (165, 187, 223), (72, 53, 49)]
circle = Turtle()
circle.hideturtle()
t.colormode(255)
circle.speed("fastest")
y_position = -225
circle.pensize(20)


def draw_position(p_x, p_y):
    circle.penup()
    circle.setx(p_x)
    circle.sety(p_y)
    circle.pendown()


def draw_color():
    circle.color(random.choice(color_list))
    circle.forward(1)
    circle.penup()
    circle.forward(50)
    circle.pendown()


while y_position <= 225:
    draw_position(-225, y_position)
    y_position += 50
    for i in range(10):
        draw_color()


screen = Screen()
screen.exitonclick()
