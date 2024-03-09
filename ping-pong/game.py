import arcade

class Ball(arcade.Spite):
    pass 

class GameWindow(arcade.Window):
    def __init__(self,witht,height,title):
        super().__init__(witht,height,title)
        self.ball = Ball()
        
        
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((162,124,167))

    
    
window = GameWindow(700, 500, "Ping-Pong")
arcade.run()