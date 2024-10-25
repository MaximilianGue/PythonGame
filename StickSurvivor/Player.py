from Bullet import Bullet

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from Clock import Clock
from Healthbar import Healthbar


class Player:

    # Constructor
    def __init__(self, position, playerspeed, jumpspeed):
        self.position = Vector(*position)  # current position

        # adjustable
        self.playerspeed = playerspeed
        self.jump_speed = jumpspeed

        self.ground = position

        self.load_sprites()
        self.looking_right = True


        ### IMG
        self.dims = (512, 512)
        self.current_image = simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0001.png")

        ### Jumping
        self.is_jumping = False ## no timpl
        self.gravity = 0.02
        self.can_jump = True
        self.upwards_force = 0.05
        self.max_height = None
        self.counter_in_jump = 0

        ### Dash
        self.counter_for_dash = 0
        self.isdashing = False
        self.counter_after_dash_start = 0

        ### Shooting
        self.bullet = None
        self.counter_for_bullet = 0
        self.can_shoot = True
        self.isshooting = False

        #hitting
        self.can_hit = False
        self.counter_in_hit = 0

        #sword
        self.counter_with_sword = 0
        self.can_sword = True

        #clock
        self.clocks = []
        self.load_clocks()

        #health
        self.health = 3
        self.healthbar_cons = -40
        self.healthbar = Healthbar(3, (self.position.get_x(), self.position.get_y() + self.healthbar_cons))

        self.swang_sword = False
        self.swang_fists = False

        self.load_sounds()

    # loading sprites and appending them to sprite lists and initalizing counters
    def load_sprites(self):
         ### Running
        self.running = [] #Sprite sheet (8 Sprites)
        self.running_left = []
        self.current_sprite = 0
        self.counter = 0
        self.count_until_when = 3

        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0017.png"))
        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0018.png"))
        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0019.png"))
        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0020.png"))
        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0021.png"))
        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0022.png"))
        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0023.png"))
        self.running.append(simplegui._load_local_image("Assets/PlayerSprites/running/fighter_run_0024.png"))

        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0017-modified.png"))
        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0018-modified.png"))
        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0019-modified.png"))
        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0020-modified.png"))
        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0021-modified.png"))
        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0022-modified.png"))
        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0023-modified.png"))
        self.running_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/running_left/fighter_run_0024-modified.png"))

        ### Idle
        self.idle = []
        self.idle_left = []
        self.current_sprite_idle = 0
        self.counter_idle = 0
        self.count_until_idle = 5

        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0001.png"))
        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0002.png"))
        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0003.png"))
        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0004.png"))
        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0005.png"))
        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0006.png"))
        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0007.png"))
        self.idle.append(simplegui._load_local_image("Assets/PlayerSprites/Idle/fighter_Idle_0008.png"))

        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0001-modified.png"))
        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0002-modified.png"))
        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0003-modified.png"))
        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0004-modified.png"))
        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0005-modified.png"))
        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0006-modified.png"))
        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0007-modified.png"))
        self.idle_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Idle_left/fighter_Idle_0008-modified.png"))

        self.jump_right = []
        self.jump_left = []
        self.current_sprite_jump = 0
        self.counter_jump = 0


        self.jump_right.append(simplegui._load_local_image("Assets/PlayerSprites/jump/fighter_jump_0043.png")) #charge
        self.jump_right.append(simplegui._load_local_image("Assets/PlayerSprites/jump/fighter_jump_0044.png")) #charge
        self.jump_right.append(simplegui._load_local_image("Assets/PlayerSprites/jump/fighter_jump_0045.png")) #drop
        self.jump_right.append(simplegui._load_local_image("Assets/PlayerSprites/jump/fighter_jump_0046.png"))
        self.jump_right.append(simplegui._load_local_image("Assets/PlayerSprites/jump/fighter_jump_0047.png"))

        self.jump_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/jump_left/fighter_jump_0043-modified.png"))
        self.jump_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/jump_left/fighter_jump_0044-modified.png"))
        self.jump_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/jump_left/fighter_jump_0045-modified.png"))
        self.jump_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/jump_left/fighter_jump_0046-modified.png"))
        self.jump_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/jump_left/fighter_jump_0047-modified.png"))

        self.dash_right = []
        self.dash_left = []
        self.current_sprite_dash = 0
        # counter for dash --> from constuctor

        self.dash_right.append(simplegui._load_local_image("Assets/PlayerSprites/Dash/fighter_dash_0033.png"))
        self.dash_right.append(simplegui._load_local_image("Assets/PlayerSprites/Dash/fighter_dash_0034.png"))
        self.dash_right.append(simplegui._load_local_image("Assets/PlayerSprites/Dash/fighter_dash_0035.png"))
        self.dash_right.append(simplegui._load_local_image("Assets/PlayerSprites/Dash/fighter_dash_0036.png"))
        self.dash_right.append(simplegui._load_local_image("Assets/PlayerSprites/Dash/fighter_dash_0037.png"))
        self.dash_right.append(simplegui._load_local_image("Assets/PlayerSprites/Dash/fighter_dash_0038.png"))

        self.dash_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Dash_left/fighter_dash_0033-modified.png"))
        self.dash_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Dash_left/fighter_dash_0034-modified.png"))
        self.dash_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Dash_left/fighter_dash_0035-modified.png"))
        self.dash_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Dash_left/fighter_dash_0036-modified.png"))
        self.dash_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Dash_left/fighter_dash_0037-modified.png"))
        self.dash_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/Dash_left/fighter_dash_0038-modified.png"))

        self.shootsprites = []
        self.counter_for_bullet_sprites = 0
        self.shootsprites.append(simplegui._load_local_image("Assets/PlayerSprites/shoot/pistol_shot_0064.png"))
        self.shootsprites.append(simplegui._load_local_image("Assets/PlayerSprites/shoot/pistol_shot_0065.png"))

        self.shootsprites_left = []
        self.shootsprites_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/shoot_left/pistol_shot_0064-modified.png"))
        self.shootsprites_left.append(simplegui._load_local_image(
            "Assets/PlayerSprites/shoot_left/pistol_shot_0065-modified.png"))

        self.combo_right = []
        self.current_combo_sprite = 0

        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0064.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0065.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0066.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0067.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0068.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0069.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0070.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0071.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0072.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0073.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0074.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0075.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0076.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0077.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0078.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0079.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0080.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0081.png")))
        self.combo_right.append((simplegui._load_local_image("Assets/PlayerSprites/hit/fighter_combo_0082.png")))

        self.combo_left = []

        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0064-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0065-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0066-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0067-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0068-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0069-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0070-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0071-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0072-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0073-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0074-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0075-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0076-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0077-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0078-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0079-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0080-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0081-modified.png")))
        self.combo_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/hit_left/fighter_combo_0082-modified.png")))

        self.combo_sword = []
        self.current_sword_sprite = 0

        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0065.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0066.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0067.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0068.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0069.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0070.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0071.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0072.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0073.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0074.png"))
        self.combo_sword.append(simplegui._load_local_image("Assets/PlayerSprites/sword/sword_combo_0075.png"))

        self.combo_sword_left = []

        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0065-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0066-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0067-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0068-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0069-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0070-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0071-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0072-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0073-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0074-modified.png")))
        self.combo_sword_left.append((simplegui._load_local_image(
            "Assets/PlayerSprites/sword_left/sword_combo_0075-modified.png")))

        self.death = []
        self.counter_for_death_sprites = 0
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0052.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0053.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0054.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0055.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0056.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0057.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0058.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0059.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0060.png"))
        self.death.append(simplegui._load_local_image("Assets/PlayerSprites/Death/fighter_death_0061.png"))

    # loading sounds and storing appending them to lists and initializing counter variable
    def load_sounds(self):
        self.gunshot_sound = simplegui._load_local_sound("music/12-Gauge-Pump-Action-Shotgun-Close-Gunshot-B-www.fesliyanstudios.com.mp3")
        self.sword_sounds = [] # needed for the sword sound "animation"
        self.sword_sounds.append(simplegui._load_local_sound("music/clean-fast-swooshaiff-14784.mp3"))
        self.sword_sounds.append(simplegui._load_local_sound("music/clean-fast-swooshaiff-14784.mp3"))
        self.sword_sounds.append(simplegui._load_local_sound("music/clean-fast-swooshaiff-14784.mp3"))
        self.sword_sound_counter = 0
        self.death_sound = simplegui._load_local_sound("music/breeze-of-blood-122253.mp3")
        self.dash_sound = simplegui._load_local_sound("music/rapid-wind-sound-effect-1-108398.mp3")

    # load clocks - control cooldowns and animations
    def load_clocks(self):
        c0 = Clock()                # cooldown for shooting
        c1 = Clock()                # cooldown for dash
        c2 = Clock()                # cooldown for sword
        self.clocks.append(c0)
        self.clocks.append(c1)
        self.clocks.append(c2)
        self.c3 = Clock()
        self.c3.start()

        c4 = Clock()
        c4.start()
        self.clocks.append(c4)

    # Idle animation -
    def Idle_(self):
        # iterates through the animation sprites
        self.current_sprite = 0
        self.counter_idle += 1

        if self.looking_right:
            if self.counter_idle % self.count_until_idle == 0:
                if self.current_sprite_idle < len(self.idle) - 1:
                    self.current_sprite_idle += 1
                else:
                     self.current_sprite_idle = 0
                if not self.is_jumping:
                    self.current_image = self.idle[self.current_sprite_idle]

        elif not self.looking_right:
            if self.counter_idle % self.count_until_idle == 0:
                if self.current_sprite_idle < len(self.idle_left) - 1:
                    self.current_sprite_idle += 1
                else:
                    self.current_sprite_idle = 0
                if not self.is_jumping:
                    self.current_image = self.idle_left[self.current_sprite_idle]

    # stepleft and stepright functions update the position vector of the player and take care of the running animation
    def stepleft(self):

        self.current_sprite_idle = 0
        self.looking_right = False
        self.counter += 1

        self.position.subtract(Vector(self.playerspeed, 0))
        if self.counter % self.count_until_when == 0:
            if self.current_sprite < len(self.running) - 1:
                self.current_sprite += 1
            else:
                self.current_sprite = 0
        if not self.is_jumping:
            self.current_image = self.running_left[self.current_sprite]
    def stepright(self):

        self.current_sprite_idle = 0
        self.looking_right = True
        self.counter += 1

        self.position.add(Vector(self.playerspeed, 0))
        if self.counter % self.count_until_when == 0:
            if self.current_sprite < len(self.running) - 1:
                self.current_sprite += 1
            else:
                self.current_sprite = 0
        if not self.is_jumping:
            self.current_image = self.running[self.current_sprite]


    def update(self):
        # updates the healthbar
        self.healthbar.update((self.position.get_x(), self.position.get_y() + self.healthbar_cons), self.health)

        # checks if player is still alive
        if self.health > 0:
            self.swang_sword = False
            self.swang_fists = False

            self.borders() # takes care that the player can walk out of the left and spawn on the right side and vice versa

            # cooldown of gun - 3 seconds (180 frames)
            if self.clocks[0].transition(180):
                self.can_shoot = True
                self.clocks[0].stopp()
            # cooldown of sword - 3 seconds (180 frames)
            if self.clocks[2].transition(180):
                self.can_sword = True

            # checks if the player is currently not dashing
            if not self.isdashing:

                #checks if player is on the ground
                if self.position.get_y() == 435:
                    self.can_jump = True
                    self.is_jumping = False

                # check if player is on the top of his jump
                elif self.max_height == self.position.get_y():
                    self.max_height = None
                    self.is_jumping = True

                # check if player is on the way up to the top of his jump
                elif self.max_height is not None:
                    self.jump()
                    self.is_jumping = True

                    # checks in what direction the player is looking -> updates sprite
                    if self.looking_right:
                        self.current_image = self.jump_right[1]
                    elif not self.looking_right:
                        self.current_image = self.jump_left[1]

                # player is falling
                else:
                    self.can_jump = False
                    self.fall()
                    self.is_jumping = True

                    # checks in what direction the player is looking -> updates sprite
                    if self.looking_right:
                        self.current_image = self.jump_right[2]
                    elif not self.looking_right:
                        self.current_image = self.jump_left[2]

            # player is dashing - animation and updates player position
            else:
                # dash sound
                self.dash_sound.play()

                self.counter_after_dash_start += 1
                if self.counter_after_dash_start % 3 == 0 and self.current_sprite_dash <= 5:
                    if self.looking_right:
                        self.position.add(Vector(self.playerspeed * 5, 0))
                        self.current_image = self.dash_right[self.current_sprite_dash]

                    elif not self.looking_right:
                        self.position.subtract(Vector(self.playerspeed* 5, 0))
                        self.current_image = self.dash_left[self.current_sprite_dash]

                    self.current_sprite_dash += 1
                elif self.current_sprite_dash > 5:
                    self.isdashing = False
                    self.current_sprite_dash = 0
                else:
                    pass

        # player is dead
        else:
            # death sound
            self.death_sound.play()

            # death animation
            self.c3.tick()
            if len(self.death) - 1  <= self.counter_for_death_sprites:
                self.c3.stopp()

            if self.c3.transition(5):
                self.counter_for_death_sprites += 1
            self.current_image = self.death[self.counter_for_death_sprites]


    # Jump logic
    def jump_check(self):

        # if player can jump and the button is pressed long enough the players position Vector gets updated (y axis)
        if self.can_jump:
            self.counter_jump += 1

            if self.counter_jump % 26 == 0:
                self.can_jump = False
                self.max_height = self.position.get_y() - self.jump_speed
                self.position.add(Vector(0, self.jump_speed * -self.upwards_force))

            else:
                if self.looking_right:
                    self.current_image = self.jump_right[0]
                elif not self.looking_right:
                    self.current_image = self.jump_left[0]

    # adds a positive Vector in order for the player to jump
    def jump(self):
        self.position.add(Vector(0, self.jump_speed * -self.upwards_force))
    # adds a positive Vector in order for the player to fall
    def fall(self):
        self.position.add(Vector(0, self.jump_speed * self.gravity))

    # Dash
    def dash(self):
        # player can dash every 3 seconds
        if self.clocks[1].transition(180) or self.clocks[1].is_stopped is True:
            self.isdashing = True
            self.clocks[1].start()


    def shoot(self):

        #checks if player can shoot and is not currently jumping -> player can't shoot in the air
        if self.can_shoot and not self.is_jumping:

            # animation
            self.counter_for_bullet_sprites += 1
            if self.looking_right:
                    self.current_image = self.shootsprites[1]
            else:
                    self.current_image = self.shootsprites_left[1]

            if self.counter_for_bullet_sprites / 20 == 1:
                if self.looking_right:
                    self.current_image = self.shootsprites[0]
                else:
                    self.current_image = self.shootsprites_left[0]

            elif self.counter_for_bullet_sprites / 40 == 1:

                if self.looking_right:
                    self.current_image = self.shootsprites[1]
                else:
                    self.current_image = self.shootsprites_left[1]

                # spawns bullet in the direction in which the player is facing
                if self.looking_right:
                    self.bullet = Bullet(10, (self.position.get_x() + 55, self.position.get_y() + 15), True)
                else:
                    self.bullet = Bullet(10, (self.position.get_x() - 55, self.position.get_y() + 15), False)

                # gun shot sound
                self.gunshot_sound.play()
                self.counter_for_bullet_sprites = 0
                self.counter_for_bullet = 0
                self.clocks[0].start()

                # set can_shoot to False -> player cant shoot instantly after again and has to wait for the cooldown
                self.can_shoot = False
        else:
            pass

    def hit_with_sword(self):

        # animation of sword and sets swang_sword to True
        if self.can_sword:
            self.counter_with_sword += 1

            # End of animation -> change variables and set can_sword to False -> Player cant use his sword directly after
            # and instead has to wait for the cooldown of his sword
            if self.current_sword_sprite == len(self.combo_sword):
                self.current_sword_sprite = 0
                self.clocks[2].start()
                self.can_sword = False
                self.swang_sword = True
                self.sword_sound_counter = 0

            if self.counter_with_sword % 5 == 0:
                #play sound every 15 seconds but maximumm 3 times
                if self.counter_with_sword % 15 == 0 and self.sword_sound_counter < 3:
                    self.sword_sounds[self.sword_sound_counter].play()
                    self.sword_sound_counter += 1
                # updates current image of Player considering the direction the player is looking at
                if self.looking_right:
                    self.current_image = self.combo_sword[self.current_sword_sprite]
                else:
                    self.current_image = self.combo_sword_left[self.current_sword_sprite]

                self.current_sword_sprite += 1

    def hit(self):
        # no cooldown - player can theoretically spam this attack

        # animation of the player's fist combo
        self.counter_in_hit += 1

        #end of animation
        if self.current_combo_sprite == len(self.combo_right):
            self.current_combo_sprite = 0
            self.swang_fists = True

        if self.counter_in_hit % 3 == 0:
            # update current image of Player under aspect in which diretion he is looking in
            if self.looking_right:
                self.current_image = self.combo_right[self.current_combo_sprite]
            else:
                self.current_image = self.combo_left[self.current_combo_sprite]
            self.current_combo_sprite += 1
            self.counter_in_hit = 0

    # takes care that the player can walk out of the left and spawn on the right side and vice versa
    def borders(self):
        if self.position.get_x() > 800:
            self.position = Vector(0, self.position.get_y())
        elif self.position.get_x() < 0:
            self.position = Vector(800, self.position.get_y())

    # calls update function and draws the current image of the Player
    # and a bullet if he has already shot one -> bullet != None
    def draw(self, canvas):

        self.update()
        # Flip the image horizontally is not possible rn - double the sprites rn
        canvas.draw_image(self.current_image, (self.dims[0] // 2, self.dims[1] // 2),
                          self.dims, self.position.get_p(), (self.dims[0] / 2, self.dims[1] / 2),
                          0)
        self.healthbar.draw(canvas)

        if self.bullet != None:
            self.bullet.draw(canvas)
