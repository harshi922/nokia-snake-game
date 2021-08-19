from turtle import Turtle
from scoreboard import Score

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Score):

    def __init__(self):
        super().__init__()
        self.snake_bits = []
        self.create_snake()
        self.head = self.snake_bits[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_snake_bit(position)

    def move(self):
        for snake_bit_num in range(len(self.snake_bits) - 1, 0, -1):
            new_x_pos = self.snake_bits[snake_bit_num - 1].xcor()
            new_y_pos = self.snake_bits[snake_bit_num - 1].ycor()
            self.snake_bits[snake_bit_num].goto(new_x_pos, new_y_pos)
        self.snake_bits[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_snake_bit(self, position):
        new_snake_bit = Turtle(shape="square")
        new_snake_bit.color("azure")
        new_snake_bit.penup()
        new_snake_bit.goto(position)
        self.snake_bits.append(new_snake_bit)

    def extend(self):
        self.add_snake_bit(self.snake_bits[-1].position())
