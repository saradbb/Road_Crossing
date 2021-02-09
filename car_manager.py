STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5

from car import Car
import random

class Car_Manager:
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        """
        Creates and places a car with 50% probability
        :return:
        """
        num = random.randint(0,1)
        if num == 0:
            car = Car()
            self.car_list.append(car)
    def move_cars(self,player):
        """
        Moves all the cars by designated speed, checks if the car and player collide and removes cars not in the view
        :param player:
        :return:
        """
        for cars in self.car_list:
            cars.move(self.speed)
            if cars.distance(player) < 20:
                return -1
            if cars.xcor() < -350:
                self.car_list.remove(cars)
                del cars

    def increase_level(self):
        """
        Removes the Cars.
        :return:
        """
        for car in self.car_list:
            car.hideturtle()
            del car
        self.speed += MOVE_INCREMENT












