STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        #print("Player Created")

    def move_up(self):
        #print("CALLED")
        self.forward(MOVE_DISTANCE)

    def increase_level(self):
        self.goto(STARTING_POSITION)
