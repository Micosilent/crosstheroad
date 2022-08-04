import random

from car import Car


class CarManager:
    spawn_offset = 20
    y_max = 250
    y_min = -250

    car_delta = 5
    velocity_delta = 5

    spawn_locations = []

    for spawn_y_cord in range(y_min, y_max, spawn_offset):
        spawn_locations.append(spawn_y_cord)

    def __init__(self):
        self.cars = []
        self.max_velocity = 5
        self.max_cars = 5

    def spawn_car(self):
        y_coord = random.choice(self.spawn_locations)
        self.cars.append(Car(y_coord, self.max_velocity))

    def reuse_car(self):
        for car in self.cars:
            if car.xcor() <= -300:
                car.reuse()

    def advance_cars(self):
        for car in self.cars:
            car.advance()

    def tick(self):
        if len(self.cars) < self.max_cars:
            self.spawn_car()

        self.advance_cars()
        self.reuse_car()

    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def increase_difficulty(self):
        self.max_cars += self.car_delta
        self.max_velocity += self.velocity_delta

