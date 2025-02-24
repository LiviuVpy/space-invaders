import time
from turtle import Screen

from player_ship import PlayerShip
from enemy import EnemyShips, Boss
from scoreboard import Scoreboard
from meteorites import Meteorites

class SpaceInvaders():
    def __init__(self):
        self.background_image_image = "space_invaders\\background\\background_img800x1200.png"
        self.enemy_image = "space_invaders\\alien_ships\\alien_ship_resized555.gif"
        self.alien_rocket_image = "space_invaders\\alien_ships\\alien_rocket_resized.gif"
        self.meteorite_image = "space_invaders\\meteorites\\1.gif"
        self.boss_image = "space_invaders\\alien_ships\\111boss_rm.gif"
        self.boss_rocket_image = "space_invaders\\alien_ships\\boss_rocket_resized.gif"
        
        self.screen = Screen ()
        self.screen.title("Space Invaders")
        self.screen.setup(width=800, height=1200)
        self.screen.bgpic(self.background_image_image)
        self.screen.register_shape(self.enemy_image)
        self.screen.register_shape(self.alien_rocket_image)
        self.screen.register_shape(self.meteorite_image)
        self.screen.register_shape(self.boss_image)
        self.screen.register_shape(self.boss_rocket_image)
        self.screen.tracer(0)

        self.player = PlayerShip()
        self.alien_fleet = EnemyShips()
        self.scoreboard = Scoreboard() 
        self.meteorite = Meteorites()
        self.boss = Boss()
        
        self.screen.listen()
        self.screen.onkeypress(self.player.move_right, "Right")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.fire_rocket, "space")
        
        self.game_is_on = True
        
        while self.game_is_on:

            self.screen.update()
            time.sleep(0.1)
            self.player.move_rockets()
            self.alien_fleet.move_fleet()
            self.alien_fleet.enemy_ship_fire()
            self.alien_fleet.move_alien_rockets()
            self.meteorite.create_meteorite()
            self.meteorite.move_meteorite() 
            self.meteorite.delete_meteorite()

            # introducing the boss ship:
            if len(self.alien_fleet.alien_ships) < 10:
                if self.boss.is_boss:
                    self.boss.create_mothership()
                    self.boss.move_boss()
                    self.boss.boss_ship_fire()
                    self.boss.move_rockets()
                    self.boss.move_life()

                    # detect collision boss rockets with player ship:
                    for boss_rocket in self.boss.boss_rockets_fired:
                        if boss_rocket.distance(self.player) < 25:
                            self.boss.delete_boss_rocket(boss_rocket)
                            self.scoreboard.player_ship_hit()
                            self.player.reset_position()

                        # detect collision boss rockets with meteorites:
                        for meteor in self.meteorite.meteorites:
                            if boss_rocket.distance(meteor) < 135:
                                self.boss.delete_boss_rocket(boss_rocket)

                    # detect collision player rockets with boss:
                    for player_rocket in self.player.fired_rockets:
                        for boss_ship in self.boss.mothership:
                            if player_rocket.distance(boss_ship) < 50:
                                self.player.destroy_rocket(player_rocket)
                                self.boss.delete_boss_life()
                                if self.boss.life < 1:
                                    self.boss.delete_boss_ship(boss_ship)
                                    self.scoreboard.increase_boss_score()

                # if boss dead but still flying rockets:
                else:
                    if self.meteorite.meteorites:
                        if boss_rocket.distance(meteor) < 135:
                            self.boss.delete_boss_rocket(boss_rocket)
                    if self.boss.boss_rockets_fired:
                        for boss_rocket in self.boss.boss_rockets_fired:
                            if boss_rocket.distance(self.player) < 25:
                                self.boss.delete_boss_rocket(boss_rocket)
                                self.scoreboard.player_ship_hit()
                                self.player.reset_position()
                        self.boss.move_rockets()
            
            # detect collision rockets with enemy ships:
            for ship in self.alien_fleet.alien_ships:
                for rocket in self.player.fired_rockets:
                    if ship.distance(rocket) < 30:
                        self.alien_fleet.delete_ship(ship)
                        self.player.destroy_rocket(rocket)
                        self.scoreboard.increase_score()
            
            # detect collision enemy bullets with player ship:
            for bullet in self.alien_fleet.fired_alien_rockets:
                if bullet.distance(self.player) < 25:
                    self.alien_fleet.delete_alien_rocket(bullet)
                    self.scoreboard.player_ship_hit()
                    self.player.reset_position()

            # detect collision enemy bullets with meteorite:
            for bullet in self.alien_fleet.fired_alien_rockets:
                for meteor in self.meteorite.meteorites:
                    if bullet.distance(meteor) < 135:
                        self.alien_fleet.delete_alien_rocket(bullet)

            # detect collision player rockets with meteorite:
            for rocket in self.player.fired_rockets:
                for meteor in self.meteorite.meteorites:
                    if rocket.distance(meteor) < 135:
                        self.player.destroy_rocket(rocket)

            # game lost
            if len(self.scoreboard.player_lives) < 1:
                self.game_on = False
                self.scoreboard.game_over()
                self.scoreboard.reset_score()
                break

            # game won
            if len(self.alien_fleet.alien_ships) < 1 and len(self.boss.mothership) < 1 and self.boss.is_boss == False:
                self.game_on = False
                self.scoreboard.game_won()
                self.scoreboard.reset_score()
                break

        self.screen.exitonclick()
   

if __name__ == "__main__":    
    app = SpaceInvaders()
