try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Constructor
class BackStory:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.image = None
        self.load_sprites()

    # loads background images
    def load_sprites(self):
        self.story_images = []
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory0.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory1.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory2.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory3.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory4.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory5.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory6.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory7.png"))
        self.story_images.append(simplegui._load_local_image("Assets/BackStory/backstory8.png"))

        self.story_counter = 0

        self.done = False



    def draw(self, canvas):

            self.image = self.story_images[self.story_counter]

            canvas.draw_image(self.image,
                                (self.image.get_width() / 2, self.image.get_height() / 2),
                                (self.image.get_width(), self.image.get_height()),
                                (self.width / 2, self.height / 2),
                                (self.width, self.height))


    # every mouseclick on the screen increases the story counter -> next story slide is drawn
    def mouse_click(self, pos):
        button_pos = (0, 0)
        button_size = (800, 600)

        if (button_pos[0] <= pos[0] <= button_pos[0] + button_size[0] and
                button_pos[1] <= pos[1] <= button_pos[1] + button_size[1]):

            if self.story_counter < 8:
                self.story_counter += 1
            else:
                self.done = True


