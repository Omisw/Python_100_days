from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.random_car = random.randint(1, 3)
        self.speed_level = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def new_car(self):
        random_car = random.randint(1, 5)
        if random_car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-220, 220))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed_level)

    def next_lv_move_cars(self):
        self.speed_level += MOVE_INCREMENT
