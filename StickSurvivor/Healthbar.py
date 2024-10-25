try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Healthbar:

    #Constructor
    def __init__(self, health, position):

        self.health = health
        self.position = position

        self.load_sprites()
        self.image = self.healthbar[0]
        self.dims = (152 ,50)               #dimensions of the healthbars sprites

    # loads healthbar sprites
    def load_sprites(self):
        self.healthbar = []
        self.healthbar.append(simplegui._load_local_image("Assets/Healthbar/No_life.png"))
        self.healthbar.append(simplegui._load_local_image("Assets/Healthbar/One_life.png"))
        self.healthbar.append(simplegui._load_local_image("Assets/Healthbar/Two_lives.png"))
        self.healthbar.append(simplegui._load_local_image("Assets/Healthbar/Three_lives.png"))

    # updates healthbar image according to the parameter health - used for the players health
    def update(self, position, health):
        self.position = position

        match health:
            case 0:
                self.image = self.healthbar[0]
            case 1:
                self.image = self.healthbar[1]
            case 2:
                self.image = self.healthbar[2]
            case 3:
                self.image = self.healthbar[3]

    # setter method
    def set_health(self, health):
        self.health = health

    # draws the healtbar
    def draw(self, canvas):
        canvas.draw_image(self.image, (self.dims[0] // 2, self.dims[1] // 2),
                          self.dims, self.position, (self.dims[0] / 2, self.dims[1] / 2),
                          0)
