import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("tertle")
screen.tracer(0)


car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


# EVENT BINDINGS GO HERE
screen.onkey(player.move_forward, "w")
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")

screen.listen()

game_is_on = True

while game_is_on:

    car_manager.tick()
    collision = car_manager.check_collision(player)

    if collision:
        scoreboard.game_over()
        game_is_on = False

    if player.ycor() > 280:
        scoreboard.increment()
        player.move_to_start()
        car_manager.increase_difficulty()

    time.sleep(0.016)
    screen.update()

screen.exitonclick()
