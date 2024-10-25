try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Backgrounds:
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self.image = simplegui._load_local_image("Assets/Backgrounds/main.png")
        self.load_images()

    def load_images(self):
        self.background_images = []
        self.background_images.append(simplegui._load_local_image("Assets/Backgrounds/main.png"))
        self.background_images.append(simplegui._load_local_image("Assets/Backgrounds/image0.png"))
        self.background_images.append(simplegui._load_local_image("Assets/Backgrounds/image1.png"))


    def draw(self, canvas):
        canvas.draw_image(self.image,
                  (self.image.get_width() / 2, self.image.get_height() / 2),
                  (self.image.get_width(), self.image.get_height()),
                  (self.width / 2, self.height / 2),
                  (self.width, self.height))

    def change_background(self, num):
        if num == 0:
            self.image = self.background_images[0]
        elif num == 1:
            self.image = self.background_images[1]
        elif num == 2:
            self.image = self.background_images[2]

