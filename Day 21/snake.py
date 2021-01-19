from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment_snake = []
        self.create_snake()
        self.head = self.segment_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(x=position)
        self.segment_snake.append(snake)

    def extend(self):
        self.add_segment(self.segment_snake[-1].position())

    def move(self):
        for segment in range(len(self.segment_snake) - 1, 0, -1):
            new_x = self.segment_snake[segment - 1].xcor()
            new_y = self.segment_snake[segment - 1].ycor()
            self.segment_snake[segment].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
