
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

X_POS = 290
Y_MIN = -250
Y_MAX = 250

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()    #Hide until at right position
        self.shape('square')

        self.penup()
        self.get_position_and_color()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.speed(0)    #Fastest
        self.showturtle()

    def get_position_and_color(self):
        """
        Puts the car in random place and selects a random color
        :return:
        """
        self.setpos(X_POS,random.randint(Y_MIN,Y_MAX))
        self.color(random.choice(COLORS))


    def move(self,steps):
        """
        Moves forward by given steps.
        :param speed:
        :return:
        """
        self.back(steps)