from turtle import Turtle

LIVES = 3
FONT = ('Courier', 12, 'normal')
LIVES_X = -370
LIVES_Y = -570

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives_image = "space_invaders\\player_ships\\lives_img.gif"
        self.screen.register_shape(self.lives_image)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = LIVES
        self.player_lives = []
        self.high_score = self.get_high_score()
        self.update_scoreboard()
        self.display_lives()

    def update_scoreboard(self):
        self.clear()
        self.goto(-370, 580)
        self.write(f'SCORE: {self.score}', align="left", font=FONT)
        self.goto(370, 580)
        self.write(f'HIGH SCORE: {self.high_score}', align = "right", font=FONT)
        
    def display_lives(self):
        n = 0
        for i in range(self.lives):
            life_item = Turtle(self.lives_image)
            life_item.penup()
            life_item.goto(LIVES_X + n, LIVES_Y)
            n+=50
            self.player_lives.append(life_item)
           
    def player_ship_hit(self):
        self.lives -= 1
        if self.player_lives:
            self.player_lives[-1].goto(860,1260)
            self.player_lives.pop()
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def increase_boss_score(self):
        self.score += 5
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align = "center", font=('Courier', 24, 'normal'))

    def game_won(self):
        self.goto(0, 0)
        self.write('YOU WON!', align = "center", font=('Courier', 24, 'normal'))

    def reset_score(self):
        if self.score > int(self.high_score):
              self.high_score = self.score
        self.score = 0
        self.write_high_score()

    def get_high_score(self):
        with open("space_invaders\\high_score.txt", 'r') as file:
                contents = file.read()
                return contents
    
    def write_high_score(self):
        with open("space_invaders\\high_score.txt", 'w') as file:
            file.write(str(self.high_score))
