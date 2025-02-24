import random
from turtle import Turtle

METEORITE_MOVE_DISTANCE = 5

class Meteorites():
    def __init__(self):
        self.meteorite_image = "space_invaders\\meteorites\\1.gif"
        self.meteorite_speed = METEORITE_MOVE_DISTANCE
        self.meteorites = []
        
    def create_meteorite(self):
        random_chance = random.randint(1,10)
        if len(self.meteorites) < 1:
            if random_chance == 1:
                new_meteorite = Turtle(self.meteorite_image)
                new_meteorite.penup()
                random_y = random.randint(-200, 50)
                new_meteorite.goto(600, random_y)
                self.meteorites.append(new_meteorite)

    def move_meteorite(self):
        for meteorite in self.meteorites:
            meteorite.backward(self.meteorite_speed)

    def delete_meteorite(self):
        for meteorite in self.meteorites:
            if meteorite.xcor() < -600:
                self.meteorites.remove(meteorite)