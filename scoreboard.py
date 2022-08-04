from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(0, 280)

        self.score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        scoreboard_text = "Score: {}".format(self.score)
        self.write(scoreboard_text,
                   False,
                   "center",
                   ("Arial", 12, "normal"))

    def increment(self):
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        scoreboard_text = "You lost! Your score was: {}".format(self.score)
        self.color("red")

        self.write(scoreboard_text,
                   False,
                   "center",
                   ("Arial", 20, "normal"))
