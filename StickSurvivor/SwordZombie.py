from Zombie import Zombie
from Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Clock import Clock

class SwordZombie(Zombie):
    def __init__(self, position):

        super().__init__(position)
        self.zombiespeed = 2
        self.load_clocks()
        self.load_sprites()

        self.load_sounds()




    def load_sprites(self):
        #loading the zombie sprites
        self.sword_walk = []
        self.sword_walk_counter = 0
        self.sword_walk.append(simplegui._load_local_image("Assets/Zombie/Sword_walk/sword_walk_0009.png"))
        self.sword_walk.append(simplegui._load_local_image("Assets/Zombie/Sword_walk/sword_walk_0011.png"))
        self.sword_walk.append(simplegui._load_local_image("Assets/Zombie/Sword_walk/sword_walk_0012.png"))
        self.sword_walk.append(simplegui._load_local_image("Assets/Zombie/Sword_walk/sword_walk_0013.png"))
        self.sword_walk.append(simplegui._load_local_image("Assets/Zombie/Sword_walk/sword_walk_0014.png"))
        self.sword_walk.append(simplegui._load_local_image("Assets/Zombie/Sword_walk/sword_walk_0015.png"))
        self.sword_walk.append(simplegui._load_local_image("Assets/Zombie/Sword_walk/sword_walk_0016.png"))

        self.sword_walk_left = []
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0009-modified.png"))
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0010-modified.png"))
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0011-modified.png"))
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0012-modified.png"))
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0013-modified.png"))
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0014-modified.png"))
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0015-modified.png"))
        self.sword_walk_left.append(simplegui._load_local_image("Assets/Zombie/Sword_walk_left/sword_walk_0016-modified.png"))

        self.sword_idle = []
        self.sword_idle_counter = 0
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0001.png"))
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0002.png"))
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0003.png"))
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0004.png"))
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0005.png"))
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0006.png"))
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0007.png"))
        self.sword_idle.append(simplegui._load_local_image("Assets/Zombie/Sword_idle/sword_Idle_0008.png"))

        self.sword_idle_left = []
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0001-modified.png"))
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0002-modified.png"))
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0003-modified.png"))
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0004-modified.png"))
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0005-modified.png"))
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0006-modified.png"))
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0007-modified.png"))
        self.sword_idle_left.append(simplegui._load_local_image("Assets/Zombie/Sword_Idle_Left/sword_Idle_0008-modified.png"))

        self.sword_hit_counter = 0
        self.sword_hit = []
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0065.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0066.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0067.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0068.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0069.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0070.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0071.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0072.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0073.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0074.png"))
        self.sword_hit.append(simplegui._load_local_image("Assets/Zombie/Sword_hit/sword_combo_0075.png"))

        self.sword_hit_left = []
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0065-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0066-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0067-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0068-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0069-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0070-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0071-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0072-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0073-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0074-modified.png"))
        self.sword_hit_left.append(simplegui._load_local_image("Assets/Zombie/Sword_hit_left/sword_combo_0075-modified.png"))
    def load_clocks(self):
        self.clocks = []
        c0 = Clock()
        c1 = Clock()
        c2 = Clock()         #checks if zombie can hit
        c3 = Clock()
        self.clocks.append(c0)
        self.clocks.append(c1)
        self.clocks.append(c2)
        self.clocks.append(c3)
        self.clocks[2].start()
        self.clocks[3].start()

        c4 = Clock()
        self.clocks.append(c4)
        self.clocks[4].start()

    def load_sounds(self):
        self.gunshot_sound = simplegui._load_local_sound("music/12-Gauge-Pump-Action-Shotgun-Close-Gunshot-B-www.fesliyanstudios.com.mp3")
        self.sword_sounds = []
        self.sword_sounds.append(simplegui._load_local_sound("music/clean-fast-swooshaiff-14784.mp3"))
        self.sword_sounds.append(simplegui._load_local_sound("music/clean-fast-swooshaiff-14784.mp3"))
        self.sword_sounds.append(simplegui._load_local_sound("music/clean-fast-swooshaiff-14784.mp3"))
        self.sword_sound_counter = 0

    def update(self, player_pos):
        #method for moving towards the player

        if self.health == 0:
            print("Zombie dead")

        self.dealt_damage_with_Sword = False

        if self.sword_walk_counter > len(self.sword_walk) - 1:
            self.sword_walk_counter = 0

        self.clocks[2].tick()
        if self.clocks[2].transition(180):
            self.can_hit = True
            self.clocks[2].stopp()

        if self.position.get_x() <= player_pos.get_x():
            self.looking_right = True
        else:
            self.looking_right = False

        if self.position.get_x() + 50 < player_pos.get_x(): ### range for gun zombies will be different
            self.position.add(Vector(self.zombiespeed, 0))
            self.clocks[0].start()
            self.clocks[0].tick()
            self.zombie_image = self.sword_walk[self.sword_walk_counter]
            self.clocks[1].stopp()


        elif self.position.get_x() > player_pos.get_x() + 50:
            self.position.subtract(Vector(self.zombiespeed, 0))
            self.clocks[0].start()
            self.clocks[0].tick()
            self.zombie_image = self.sword_walk_left[self.sword_walk_counter]
            self.clocks[1].stopp()


        else: ### Attack only if y positions are the same - otherise idle ### maybe split sword attack into three

            y_difference = self.position.get_y() - player_pos.get_y()

            if y_difference < 10 and self.can_hit: ## Is the Player on the same level - not in  the air!
                self.clocks[3].tick()
                self.clocks[4].tick()

                if self.sword_hit_counter >= len(self.sword_hit):
                    self.sword_hit_counter = 0
                    self.can_hit = False
                    self.clocks[2].start()
                    self.dealt_damage_with_Sword = True
                    self.sword_sound_counter = 0

                if self.looking_right:
                    self.zombie_image = self.sword_hit[self.sword_hit_counter]
                else:
                    self.zombie_image = self.sword_hit_left[self.sword_hit_counter]

                if self.clocks[3].transition(5): #hit
                    self.sword_hit_counter += 1

                if self.clocks[4].transition(15) and self.sword_sound_counter <3:
                    self.sword_sounds[self.sword_sound_counter].play()
                    self.sword_sound_counter += 1






            else:
                self.clocks[0].stopp()
                self.clocks[1].start()
                self.clocks[1].tick()
                if self.sword_idle_counter >= len(self.sword_idle):
                    self.sword_idle_counter = 0

                if self.looking_right:
                    self.zombie_image = self.sword_idle[self.sword_idle_counter]
                else:
                    self.zombie_image = self.sword_idle_left[self.sword_idle_counter]


        if self.clocks[0].transition(5):
            self.sword_walk_counter += 1

        if self.clocks[1].transition(3):
            self.sword_idle_counter += 1









