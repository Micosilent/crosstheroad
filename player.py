from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.shape("turtle")
        self.velocity = 20

    def move_forward(self):
        next_x = self.xcor()
        next_y = self.ycor() + self.velocity

        self.goto(next_x, next_y)

    def move_left(self):
        next_x = self.xcor() - self.velocity
        next_y = self.ycor()

        self.goto(next_x, next_y)

    def move_right(self):
        next_x = self.xcor() + self.velocity
        next_y = self.ycor()

        self.goto(next_x, next_y)

    def move_to_start(self):
        self.goto(0, -280)