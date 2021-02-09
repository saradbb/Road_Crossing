from turtle import Turtle, Screen
import time,random
from player import Player
from car_manager import Car_Manager
from playsound import playsound
from score_board import Score_Board

#Create A player object that moves only in upper direction
#Create a car manager system that manages the inflow and outflow of cars.
# Create Level board to keep track of level
# Update Scoreboard, Player and Car Management System when promoted to next level.

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Turtle Cross")
screen.listen()
screen.tracer(0)
playsound('mario.mp3',False)   #Continuous Mario Music until exited
player = Player()
car_manager = Car_Manager()
score_board = Score_Board()
screen.onkey(key = "Up",fun = player.move_up)   #Can only move upwards




def handle_crash():
    #Once the player collides with car, Game Over.
    global game_on
    game_on = False

def level_up():
    #Reinitialize everything to start the game.
    score_board.increase_level()   #Increases score in the scoreboard
    car_manager.increase_level()   #Cleares and delete all the cars in current level, increase car speed for next level
    player.increase_level()        #Go to starting position

game_on = True   #Bool to check if the game is still in progress.

while game_on:
    car_manager.create_cars()          #Every round a random #of cars are generated. n >=0
    if car_manager.move_cars(player) == -1:     #move_cars returns -1 if the player colided with car
        handle_crash()
    if player.ycor() > 270:       #If player makes past the enedline
        level_up()
    time.sleep(0.4)       #Manage the gameplay speed.
    screen.update()


score_board.game_over()


screen.exitonclick()