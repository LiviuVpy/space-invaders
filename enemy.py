import random
from turtle import Turtle

MOVE_DISTANCE = 5
BOSS_MOVE_DISTANCE = 10
WIDTH = 800
HEIGHT = 1200
X = -250
Y = 400

class EnemyShips():
    def __init__(self):
        self.enemy_image = "space_invaders\\alien_ships\\alien_ship_resized555.gif"
        self.alien_rocket_image = "space_invaders\\alien_ships\\alien_rocket_resized.gif"
        self.alien_ships = []
        self.fired_alien_rockets = []
        self.x_move = MOVE_DISTANCE
        self.create_fleet()

    def create_fleet(self):
        for i in range(3):
            for j in range(7):
                new_y = Y-i*80
                new_x = X+j*80
                new_ship = Turtle(self.enemy_image)
                new_ship.penup()
                new_ship.goto(new_x, new_y)
                self.alien_ships.append(new_ship)
                           
    def move_fleet(self):
        for ship in self.alien_ships:
            ship.goto(x=ship.xcor() + self.x_move, y=ship.ycor())

        newlst_right = [i for i in self.alien_ships if i.xcor() > 350]
        newlst_left = [i for i in self.alien_ships if i.xcor() < -350]

        for ship in newlst_right:
            if ship.xcor() > 350:
                self.bounce_x()
                newlst_right.clear()

        for ship in newlst_left:    
            if ship.xcor() < -350:
                self.bounce_x()
                newlst_left.clear()

    def bounce_x(self):
        self.x_move *= -1
        
    def delete_ship(self, alien_ship):
        alien_ship.penup()
        alien_ship.goto(860,1260)
        self.alien_ships.remove(alien_ship)

    def enemy_ship_fire(self):
        if self.alien_ships:
            random_ship = random.randint(0, len(self.alien_ships)-1)
            fire_chance = random.randint(1,15) 
            if fire_chance == 7:
                alien_rocket = Turtle(self.alien_rocket_image) 
                alien_rocket.penup()
                alien_rocket.goto(self.alien_ships[random_ship].xcor(), self.alien_ships[random_ship].ycor())
                alien_rocket.setheading(270)
                self.fired_alien_rockets.append(alien_rocket)
    
    def move_alien_rockets(self):
        for alien_rocket in self.fired_alien_rockets:
            alien_rocket.forward(20)

    def delete_alien_rocket(self, impact_alien_rocket):
        impact_alien_rocket.penup()
        impact_alien_rocket.goto(860,1260)
        self.fired_alien_rockets.remove(impact_alien_rocket)

class Boss():
    def __init__(self):
        self.mothership = []
        self.boss_rockets_fired = []
        self.life = 3
        self.lives = []
        self.is_boss = True

    def create_mothership(self):
        if len(self.mothership) < 1:
            self.boss_image = "space_invaders\\alien_ships\\111boss_rm.gif"
            self.boss_rocket_image = "space_invaders\\alien_ships\\boss_rocket_resized.gif"
            boss_ship = Turtle(self.boss_image)
            boss_ship.penup()
            boss_ship.goto((0, 500))
            self.x_move = BOSS_MOVE_DISTANCE
            self.mothership.append(boss_ship)
            self.create_boss_life()
            
    def move_boss(self):
        boss = self.mothership[0]
        boss.goto(x=boss.xcor() + self.x_move, y=boss.ycor())
        if boss.xcor() > 330:
            self.bounce_x()
        elif boss.xcor()  < -330:
            self.bounce_x()

    def bounce_x(self):
        self.x_move *= -1

    def boss_ship_fire(self):
        fire_chance = random.randint(1,10) 
        if fire_chance == 1:
            boss_rocket = Turtle(self.boss_rocket_image)
            boss_rocket.penup()
            boss_rocket.goto(self.mothership[0].xcor(), self.mothership[0].ycor())
            boss_rocket.setheading(270)
            self.boss_rockets_fired.append(boss_rocket)  

    def move_rockets(self):
        for rocket in self.boss_rockets_fired:
            rocket.forward(20)

    def delete_boss_rocket(self, impact_boss_rocket):
        impact_boss_rocket.penup()
        impact_boss_rocket.goto(860,1260)
        self.boss_rockets_fired.remove(impact_boss_rocket)

    def delete_boss_ship(self, boss_ship):
        boss_ship.penup()
        boss_ship.goto(860,1260)
        self.mothership.remove(boss_ship)
        self.is_boss = False

    def create_boss_life(self):
        for i in range(3):
            life = Turtle("square")
            life.color('firebrick1')
            life.shapesize(stretch_wid=0.1, stretch_len=0.4)
            life.penup()
            self.lives.append(life)

    def move_life(self):
        for life_segm in self.lives:
            life_segm.goto(self.mothership[0].xcor() - self.lives.index(life_segm)*12, self.mothership[0].ycor()+55)

    def delete_boss_life(self):
        self.life -= 1
        self.lives[-1].goto(860,1260)
        self.lives.pop()
        