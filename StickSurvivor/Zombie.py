from Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Clock import Clock
import random

# parent class of GunZombie and SwordZombie
class Zombie:
    def __init__(self, position):

        self.position = Vector(*position)

        self.zombie_image = None
        self.dims = (512, 512)
        self.looking_right = True

        # health of every zombie
        self.health = 1

        self.can_hit = True

        # For gun zombie
        self.bullet = None

        # For sword Zombies
        self.dealt_damage_with_Sword = False
        self.load_zombie_sounds()

    def load_zombie_sounds(self):
        self.zombie_sounds = []
        self.zombie_sounds.append(simplegui._load_local_sound("music/Zombie_sounds/growling-zombie-104988.mp3"))
        self.zombie_sounds.append(simplegui._load_local_sound("music/Zombie_sounds/zombie-groan-95051.mp3"))
        self.zombie_sounds.append(simplegui._load_local_sound("music/Zombie_sounds/zombie-growl-3-6863.mp3"))

        self.zombie_sound_c = Clock()   # for the zombie sounds
        self.zombie_sound_c.start()

    # loading classes
    def load_clocks(self):
        pass
    def load_sprites(self):
        pass

    # updating function - gets overwritten in child classes (GunZombie and SwordZombie)
    def update(self, player_pos):
        pass

    # every 2 seconds every zombie plays a random zombie sound out of 3
    def play_sounds(self):
        self.zombie_sound_c.tick()
        if self.zombie_sound_c.transition(120):
            r_num = random.randint(0, 2)

            if r_num == 0:
                self.zombie_sounds[0].play()
            elif r_num == 1:
                self.zombie_sounds[1].play()
            elif r_num == 2:
                self.zombie_sounds[2].play()

    # drawing the zombie and call play_sounds() function and update bullet if applicable
    def draw(self, canvas):

        self.play_sounds()
        canvas.draw_image(self.zombie_image, (self.dims[0] // 2, self.dims[1] // 2),
                          self.dims, self.position.get_p(), (self.dims[0] / 2, self.dims[1] / 2),
                          0)

        if self.bullet is not None:
            self.bullet.draw(canvas)



