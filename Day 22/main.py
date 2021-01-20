from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speed_ball)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_rebound_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.wall_rebound_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_point()

screen.exitonclick()