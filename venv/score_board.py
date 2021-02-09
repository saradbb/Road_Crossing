from turtle import Turtle
import time
X_POS = -280
Y_POS = 260
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.penup()
        self.hideturtle()
        self.goto(X_POS,Y_POS)
        self.increase_level()


    def increase_level(self):
        """
        Updates the level in the score-board.
        :return:
        """
        self.current_level += 1
        self.update_level()

    def update_level(self):
        """
        Displays the current level.
        :return:
        """
        self.clear()
        self.write(f"Level: {self.current_level}", font=('Arial', 16, 'bold'))
    def game_over(self):
        """
        Displays the game over message and result in the center of screen
        :return:
        """
        self.clear()
        self.goto(-100,0)
        self.write(f"Game Over!! Level: {self.current_level}", font=('Arial', 24, 'bold'))


