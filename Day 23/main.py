import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()
    car_manager.move_cars()

    if turtle.ycor() > 260:
        scoreboard.score()
        scoreboard.level_up()
        car_manager.next_lv_move_cars()
        turtle.start_position()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
