from turtle import Turtle
STARTING_POSITION = (0, -500)
MOVE_DISTANCE = 20
ROCKETS = 1

class PlayerShip(Turtle):
    def __init__(self):
        super().__init__()
        self.player_ship_image = "space_invaders\\player_ships\\66resized.gif"
        self.screen.register_shape(self.player_ship_image)
        self.shape(self.player_ship_image)
        self.penup()
        self.reset_position() 
        self.setheading(90)
        self.fired_rockets = []

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move_right(self):
        if self.xcor()  < 340:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def fire_rocket(self):
        self.delete_rocket()
        if len(self.fired_rockets) < ROCKETS:
            self.rocket_image = "space_invaders\\player_ships\\resized.gif"
            self.screen.register_shape(self.rocket_image)
            rocket = Turtle(self.rocket_image)
            rocket.penup()
            rocket.goto(PlayerShip.xcor(self), PlayerShip.ycor(self))
            rocket.setheading(90)
            self.fired_rockets.append(rocket)

    def move_rockets(self):
        for item in self.fired_rockets:
            item.forward(30)

    def destroy_rocket(self, impact_rocket):
        impact_rocket.penup()
        impact_rocket.goto(860,1260)
        self.fired_rockets.remove(impact_rocket)
        
    def delete_rocket(self):
        for rocket in self.fired_rockets:
            if rocket.ycor() > 650:
                self.fired_rockets.remove(rocket)



