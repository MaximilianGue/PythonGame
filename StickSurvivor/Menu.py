try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# parent class of DeathScreen, MainMenu and Pause
class Menu:
    def __init__(self, width, height, score, highscore):
        self.width  = width
        self.height = height

        self.click_sound = simplegui._load_local_sound("music/mouse-click-153941.mp3")

     ## score system
        self.score = score
        self.highscore = highscore


    # sets "buttons variables" back to False
    def reset(self):
        self.play_button_pressed = False
        self.menu_button_pressed = False

    # updates scores - the score is displayed in all the child classes
    def update_scores(self, score, highscore):
        self.score = score
        self.highscore = highscore
