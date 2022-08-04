import random
from turtle import Turtle


class Car(Turtle):
    colors = ["green", "red", "blue", "brown", "purple", "pink", "grey"]

    def __init__(self, position, max_velocity):
        super().__init__()
        self.max_velocity = max_velocity
        self.position = position
        self.velocity = random.randint(2, self.max_velocity)

        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(self.colors))
        self.goto(300, self.position)
        self.setheading(180)

    def reuse(self):
        self.color(random.choice(self.colors))
        self.goto(300, self.position)
        self.velocity = random.randint(1, self.max_velocity)

    def advance(self) -> None:
        self.forward(self.velocity)

