from Zombie import Zombie
from Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Clock import Clock
from Bullet import Bullet

# inheritance from Zombie class
class GunZombie(Zombie):

    # Constructor
    def __init__(self, position):

        super().__init__(position)  # calls zombie constructor
        self.zombiespeed = 1.5      # zombiespeed

        # only one bullet per zombie
        self.bullet = None

        # checks if the zombie can hit / shoot (is the player on the ground)
        self.can_hit = False

        # loads ...
        self.load_sounds()
        self.load_clocks()
        self.load_sprites()

    # loading all the sprites needed for the gun zombie - walk (both directions), idle (both directions), shoot(both directions)
    # initializing counters so we can iterate through the zombie sprites lists
    def load_sprites(self):

        self.gun_walk = []
        self.gun_walk_counter = 0
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0009.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0010.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0011.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0011.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0012.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0013.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0014.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0015.png"))
        self.gun_walk.append(simplegui._load_local_image("Assets/Zombie/Gun_walk/pistol_walk_0016.png"))

        self.gun_walk_left = []
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0009-modified.png"))
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0010-modified.png"))
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0011-modified.png"))
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0012-modified.png"))
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0013-modified.png"))
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0014-modified.png"))
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0015-modified.png"))
        self.gun_walk_left.append(simplegui._load_local_image("Assets/Zombie/Gun_walk_left/pistol_walk_0016-modified.png"))

        self.gun_idle = []
        self.gun_idle_counter = 0
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0001.png"))
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0002.png"))
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0003.png"))
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0004.png"))
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0005.png"))
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0006.png"))
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0007.png"))
        self.gun_idle.append(simplegui._load_local_image("Assets/Zombie/Gun_idle/pistol_Idle_0008.png"))

        self.gun_idle_left = []
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0001-modified.png"))
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0002-modified.png"))
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0003-modified.png"))
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0004-modified.png"))
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0005-modified.png"))
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0006-modified.png"))
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0007-modified.png"))
        self.gun_idle_left.append(simplegui._load_local_image("Assets/Zombie/Gun_idle_left/pistol_Idle_0008-modified.png"))

        self.gun_shoot = []
        self.gun_hit_counter = 0
        self.gun_shoot.append(simplegui._load_local_image("Assets/Zombie/Gun_shoot/pistol_shot_0064.png"))
        self.gun_shoot.append(simplegui._load_local_image("Assets/Zombie/Gun_shoot/pistol_shot_0065.png"))

        self.gun_shoot_left = []
        self.gun_shoot_left.append(simplegui._load_local_image("Assets/Zombie/Gun_shoot_left/pistol_shot_0064-modified.png"))
        self.gun_shoot_left.append(simplegui._load_local_image("Assets/Zombie/Gun_shoot_left/pistol_shot_0065-modified.png"))

    # loading Clock variables
    def load_clocks(self):
        self.clocks = []
        c0 = Clock()             # for walk animation
        c1 = Clock()             # for idle animation
        c2 = Clock()             # checks if zombie can hit
        c3 = Clock()             # for shooting animation
        self.clocks.append(c0)
        self.clocks.append(c1)
        self.clocks.append(c2)
        self.clocks.append(c3)
        self.clocks[2].start()
        self.clocks[3].start()

    # loads sound for when zombie shoots
    def load_sounds(self):
        self.gunshot_sound = simplegui._load_local_sound("music/12-Gauge-Pump-Action-Shotgun-Close-Gunshot-B-www.fesliyanstudios.com.mp3")



    def update(self, player_pos):

        # checks if gun_walk_counter is to high for accessing the last element of the list and if so sets it to 0
        # (in order to repeat the animation)
        if self.gun_walk_counter >= len(self.gun_walk) - 1:
            self.gun_walk_counter = 0

        self.clocks[2].tick()
        # sets can_hit variable to True after 3 seconds (Zombie can hit/shoot every 3 seconds)
        if self.clocks[2].transition(180):
            self.can_hit = True
            self.clocks[2].stopp()

        # checks in which direction the zombie has to face - based on players position
        if self.position.get_x() <= player_pos.get_x():
            self.looking_right = True
        else:
            self.looking_right = False

        # if zombie is more than 200 x points in each direction the zombie walks towards the player (with zombiespeed)
        if self.position.get_x() + 200 < player_pos.get_x():
            self.position.add(Vector(self.zombiespeed, 0))
            self.clocks[0].start()
            self.clocks[0].tick()
            self.zombie_image = self.gun_walk[self.gun_walk_counter]
            self.clocks[1].stopp()
        elif self.position.get_x() > player_pos.get_x() + 200:
            self.position.subtract(Vector(self.zombiespeed, 0))
            self.clocks[0].start()
            self.clocks[0].tick()
            self.zombie_image = self.gun_walk_left[self.gun_walk_counter]
            self.clocks[1].stopp()

        # Zombie is within 200 x points in one direction (close enough to theoretically shoot/hit)
        else:
            # important gunzombie doesn't care about where the player is on the y - axis (unlike sword zombie) -> increases difficulty
            if self.can_hit: # checks if zombie can hit / shoot - or if the gun is still cooling down

                self.clocks[3].tick()

                # every 5 frames change of zombie image - shooting animation
                if self.clocks[3].exact_transition(0):
                    if self.looking_right:
                        self.zombie_image = self.gun_shoot[1]
                    else:
                        self.zombie_image = self.gun_shoot_left[1]

                elif self.clocks[3].exact_transition(5):
                    if self.looking_right:
                        self.zombie_image = self.gun_shoot[0]
                    else:
                        self.zombie_image = self.gun_shoot_left[0]

                # after animation is done - set can_hit to False (important for cooldown of gun)
                # and spawn of bullet object and play sound
                elif self.clocks[3].exact_transition(10):
                    if self.looking_right:
                        self.zombie_image = self.gun_shoot[1]
                    else:
                        self.zombie_image = self.gun_shoot_left[1]
                    self.can_hit = False

                    if self.looking_right:
                        b1 = Bullet(10, (self.position.get_x() + 55, self.position.get_y() + 15), True)
                    else:
                        b1 = Bullet(10, (self.position.get_x() - 55, self.position.get_y() + 15), False)

                    self.gunshot_sound.play()

                    self.bullet = b1
                    self.clocks[2].start()
                    self.clocks[3].reset()

            else:   # zombie idle - because zombie is close enough to theoretically shoot however it can't because of the gun cooldown
                self.clocks[0].stopp()
                self.clocks[1].start()
                self.clocks[1].tick()
                if self.gun_idle_counter >= len(self.gun_idle):
                    self.gun_idle_counter = 0

                # check in which way the zombie is facing (for idle animation)
                if self.looking_right:
                    self.zombie_image = self.gun_idle[self.gun_idle_counter]
                else:
                    self.zombie_image = self.gun_idle_left[self.gun_idle_counter]


        # update counters (for animations)
        if self.clocks[0].transition(5):
            self.gun_walk_counter += 1
        if self.clocks[1].transition(3):
            self.gun_idle_counter += 1




