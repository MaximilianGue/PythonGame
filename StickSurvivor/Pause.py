try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Menu import Menu


class PauseMenu(Menu): # inherits from Menu class
    def __init__(self, frame, draw_main, width, height, score, highscore):

        super().__init__(width, height, score, highscore) # calls Menu constructor

        self.frame = frame
        self.paused = False

        self.draw_main = draw_main

        self.background = simplegui._load_local_image("Assets/Backgrounds/image3.png")
        self.frame.set_mouseclick_handler(self.mouse_click)

        self.menu_button_pressed = False


    # pause sets the draw handler from the draw_main to its own draw and sets it after pause is over back to draw_main
    def pause(self):
        self.paused = not self.paused
        if self.paused:
            self.frame.set_draw_handler(self.draw)

        else:
            self.frame.set_draw_handler(self.draw_main)


    # draws the buttons (polygons), draws the text and plays the music
    def draw(self, canvas):

        canvas.draw_image(self.background,
                          (self.background.get_width() / 2, self.background.get_height() / 2),
                          (self.background.get_width(), self.background.get_height()),
                          (self.width / 2, self.height / 2),
                          (self.width, self.height))

        if self.paused and self.menu_button_pressed:
            self.paused = False
            self.frame.set_draw_handler(self.draw_main)

        if self.paused:
            canvas.draw_text("PAUSED", [305, 100 + 50], 48, "White")

            canvas.draw_text("Score: " + str(self.score), [330, 150 + 50], 24, "White")
            canvas.draw_text("HighScore: " + str(self.highscore), [330, 200 + 50], 24, "White")

            button_pos = (300, 350 + 50)
            button_size = (200,50)
            button_corners = [
                button_pos,
                (button_pos[0] + button_size[0], button_pos[1]),
                (button_pos[0] + button_size[0], button_pos[1] + button_size[1]),
                (button_pos[0], button_pos[1] + button_size[1])
            ]
            canvas.draw_polygon(button_corners, 1, "Black", "White")
            canvas.draw_text("QUIT", (button_pos[0] + 68, button_pos[1] + 32), 24, "Black")


            button_pos = (300, 250 + 50)
            button_size = (200,50)
            button_corners = [
                button_pos,
                (button_pos[0] + button_size[0], button_pos[1]),
                (button_pos[0] + button_size[0], button_pos[1] + button_size[1]),
                (button_pos[0], button_pos[1] + button_size[1])
            ]
            canvas.draw_polygon(button_corners, 1, "Black", "White")
            canvas.draw_text("MAIN MENU", (button_pos[0] + 32, button_pos[1] + 32), 24, "Black")

    # checks if buttons are pressed and if so sets "the button_pressed" variables to true
    def mouse_click(self, pos):
        button_pos = (300, 250 + 50)
        button_size = (200, 50)

        if (button_pos[0] <= pos[0] <= button_pos[0] + button_size[0] and
                button_pos[1] <= pos[1] <= button_pos[1] + button_size[1]):

            self.click_sound.play()
            self.menu_button_pressed = True


        button_pos = (300, 350 + 50)
        button_size = (200, 50)

        if (button_pos[0] <= pos[0] <= button_pos[0] + button_size[0] and
                button_pos[1] <= pos[1] <= button_pos[1] + button_size[1]):

            self.click_sound.play()
            quit()

    # calls pause if key "p" is pressed
    def toggle_pause(self, key):
        if key == simplegui.KEY_MAP["p"]:
            self.pause()


