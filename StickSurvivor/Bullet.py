from Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Constructor
class Bullet:
    def __init__(self, bulletspeed, position, moving_right):
        self.bulletspeed = bulletspeed
        self.position = Vector(*position)       # current position
        self.startposition = Vector(*position)  # = spawn position

        #two different images for when the bullet gets shot to the left or to the right
        self.image = simplegui._load_local_image("Assets/Bullet/bullet.png")
        self.image1 = simplegui._load_local_image("Assets/Bullet/bullet-modified.png")

        self.dims = (40, 26)                # dimensions of the bullet image
        self.moving_right = moving_right    # bullet direction
        self.isdestroyed = False            # checks if the bullet is outside of the screen and can stop beeing updated



    def update(self):
        if self.moving_right: # updates bullet depending on the direction (left/right)
            self.position.set_x(self.position.get_x() + self.bulletspeed)
            if self.startposition.get_x() + 800 <= self.position.get_x():
                self.isdestroyed = True
        else:
            self.position.set_x(self.position.get_x() - self.bulletspeed)
            if self.startposition.get_x() - 800 >= self.position.get_x():
                 self.isdestroyed = True



    def draw(self, canvas):

        if self.isdestroyed is False: # stops updating and drawing the bullet if it is too far away (more than 800 from startposition)
            self.update()

            if self.moving_right:   # draws different bullet image depending on in which direction the bullet is going
                canvas.draw_image(self.image,
                                  (self.dims[0] // 2, self.dims[1] // 2),
                                  self.dims,
                                  self.position.get_p(),
                                  (self.dims[0] / 3, self.dims[1] / 3),
                                  0)
            else:
                canvas.draw_image(self.image1,
                                  (self.dims[0] // 2, self.dims[1] // 2),
                                  self.dims,
                                  self.position.get_p(),
                                  (self.dims[0] / 3, self.dims[1] / 3),
                                  0)
        else:
            pass
