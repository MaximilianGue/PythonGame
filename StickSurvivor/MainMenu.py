try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Menu import Menu

# inherits from Menu class
class MainMenu(Menu):

    # Constructor
    def __init__(self, width, height, score, highscore):

        super().__init__(width, height, score, highscore)       # calls instructor of parent class Menu

        self.background = simplegui._load_local_image("Assets/Backgrounds/image3.png")
        self.menu_music = simplegui._load_local_sound("music/Background_music/ForestWalk-320bit(chosic.com).mp3")
        self.play_button_pressed = False

    # draws the buttons (polygons), draws the text and plays the music
    def draw(self, canvas):

        self.menu_music.play()
        canvas.draw_image(self.background,
                          (self.background.get_width() / 2, self.background.get_height() / 2),
                          (self.background.get_width(), self.background.get_height()),
                          (self.width / 2, self.height / 2),
                          (self.width, self.height))

        canvas.draw_text("MAIN MENU:", [250, 100 + 50], 48, "White")
        canvas.draw_text("Score: " + str(self.score), [330, 150 + 50], 24, "White")
        canvas.draw_text("HighScore: " + str(self.highscore), [330, 200 + 50], 24, "White")

        button_pos = (300, 350 + 50)
        button_size = (200, 50)
        button_corners = [
            button_pos,
            (button_pos[0] + button_size[0], button_pos[1]),
            (button_pos[0] + button_size[0], button_pos[1] + button_size[1]),
            (button_pos[0], button_pos[1] + button_size[1])
        ]
        canvas.draw_polygon(button_corners, 1, "Black", "White")
        canvas.draw_text("QUIT", (button_pos[0] + 70, button_pos[1] + 32), 24, "Black")

        button_pos = (300, 250 + 50)
        button_size = (200, 50)
        button_corners = [
            button_pos,
            (button_pos[0] + button_size[0], button_pos[1]),
            (button_pos[0] + button_size[0], button_pos[1] + button_size[1]),
            (button_pos[0], button_pos[1] + button_size[1])
        ]
        canvas.draw_polygon(button_corners, 1, "Black", "White")
        canvas.draw_text("PLAY", (button_pos[0] + 70, button_pos[1] + 32), 24, "Black")

    # checks if buttons are pressed and if so sets "the button_pressed" variables to true
    def mouse_click(self, pos):
        button_pos = (300, 300)
        button_size = (200, 50)

        if (button_pos[0] <= pos[0] <= button_pos[0] + button_size[0] and
                button_pos[1] <= pos[1] <= button_pos[1] + button_size[1]):

            self.click_sound.play()
            self.play_button_pressed = True


        button_pos = (300, 400)
        button_size = (200, 50)

        if (button_pos[0] <= pos[0] <= button_pos[0] + button_size[0] and
                button_pos[1] <= pos[1] <= button_pos[1] + button_size[1]):

            self.click_sound.play()
            quit()



