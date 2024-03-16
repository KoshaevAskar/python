import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'PING-PONG'

SPEEDX = 5
SPEEDY = 5
BALL_IMG = 'Ping-pong'
BALL_SCORE = 0.1

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.change_x = - self.change_x 
        if self.left< 0:
            self.change_x = - self.change_x
        self.center_y += self.change_y
        if self.top> SCREEN_HEIGHT:
            self.change_y= -self.change_y
        if self.bottom<0:
            self.change_y= -self.change_y
            
            
            
            
class Platform(arcade.Sprite)
class GameWindow(arcade.Window):
    def __init__(self,witht,height,title):
        super().__init__(witht,height,title)
        self.ball = Ball(BALL_IMG, BALL_SCORE)
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.ball.change_x = SPEEDX
        self.ball.change_y = SPEEDY
        
        
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((162,124,167))
        self.ball.draw()

    
    
    def on_update(self, delta_time: float):
        self.ball.update()


window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
