try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Interaction:
    # Constructor
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard

    # calls functions of player according to which key is pressed down from the keyboard (key variables)

    def update(self):
        if self.keyboard.s_key:
            self.player.dash()
        elif self.keyboard.q_key:
            self.player.hit_with_sword()
        elif self.keyboard.e_key:
            self.player.shoot()
        elif self.keyboard.r_key:
            self.player.hit()
        elif self.keyboard.space:
            self.player.jump_check()
        elif self.keyboard.right:
            self.player.stepright()
        elif self.keyboard.left:
            self.player.stepleft()
        else:   # if no button is pressed - the player's idle function is called
            self.player.Idle_()



