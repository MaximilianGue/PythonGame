try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class GUI:

    # Constructor
    def __init__(self):
        self.load_sprites()

        self.dims = (508, 492)  # for all icons

        height = 50             # height of all the icons, because they should all be on the same height
        self.position = (675, height)
        self.position1 = (750, height)
        self.position2 = (600, height)

        # loads icons
        self.pistol_image = simplegui._load_local_image("Assets/GUI/Pistol/1-4.png")
        self.sword_image = simplegui._load_local_image("Assets/GUI/Sword/1-4.png")
        self.dash_image = simplegui._load_local_image("Assets/GUI/Dash/1-5.png")


    # loads sprites and stores them in lists
    def load_sprites(self):
        self.gun_sprites = []
        self.gun_sprites.append(simplegui._load_local_image("Assets/GUI/Pistol/1.png"))
        self.gun_sprites.append(simplegui._load_local_image("Assets/GUI/Pistol/1-2.png"))
        self.gun_sprites.append(simplegui._load_local_image("Assets/GUI/Pistol/1-3.png"))
        self.gun_sprites.append(simplegui._load_local_image("Assets/GUI/Pistol/1-4.png"))
        self.sword_sprites = []
        self.sword_sprites.append(simplegui._load_local_image("Assets/GUI/Sword/1.png"))
        self.sword_sprites.append(simplegui._load_local_image("Assets/GUI/Sword/1-2.png"))
        self.sword_sprites.append(simplegui._load_local_image("Assets/GUI/Sword/1-3.png"))
        self.sword_sprites.append(simplegui._load_local_image("Assets/GUI/Sword/1-4.png"))
        self.dash_sprites = []
        self.dash_sprites.append(simplegui._load_local_image("Assets/GUI/Dash/1-2.png"))
        self.dash_sprites.append(simplegui._load_local_image("Assets/GUI/Dash/1-3.png"))
        self.dash_sprites.append(simplegui._load_local_image("Assets/GUI/Dash/1-4.png"))
        self.dash_sprites.append(simplegui._load_local_image("Assets/GUI/Dash/1-5.png"))

    # calls the update functions of every icon
    def update(self, player_instance):
        self.update_pistol_icon(player_instance)
        self.update_sword_icon(player_instance)
        self.update_dash_icon(player_instance)

    # every icon has 4 states, 3, 2, 1 seconds cooldowns and tool useable

    # updates the pistol icon according to the 3 second (180 frames) cooldown of the gun
    def update_pistol_icon(self, player_instance):
        if player_instance.clocks[0].transition_without_reset(180) or player_instance.clocks[0].is_stopped:
            self.pistol_image = self.gun_sprites[3]


        elif player_instance.clocks[0].transition_without_reset(120):
            self.pistol_image = self.gun_sprites[2]

        elif player_instance.clocks[0].transition_without_reset(60):
            self.pistol_image = self.gun_sprites[1]

        elif player_instance.clocks[0].transition_without_reset(0):
            self.pistol_image = self.gun_sprites[0]

    # updates the sword icon according to the 3 second (180 frames) cooldown of the sword
    def update_sword_icon(self, player_instance):
        if player_instance.clocks[2].transition_without_reset(180) or player_instance.clocks[2].is_stopped:
            self.sword_image = self.sword_sprites[3]
            player_instance.clocks[2].stopp()

        elif player_instance.clocks[2].transition_without_reset(120):
            self.sword_image = self.sword_sprites[2]

        elif player_instance.clocks[2].transition_without_reset(60):
            self.sword_image = self.sword_sprites[1]

        elif player_instance.clocks[2].transition_without_reset(0):
            self.sword_image = self.sword_sprites[0]

    # updates the dash icon according to the 3 second (180 frames) cooldown of the dash
    def update_dash_icon(self, player_instance):
        if player_instance.clocks[1].transition_without_reset(180) or player_instance.clocks[1].is_stopped:
            self.dash_image = self.dash_sprites[3]
            player_instance.clocks[1].stopp()

        elif player_instance.clocks[1].transition_without_reset(120):
            self.dash_image = self.dash_sprites[2]

        elif player_instance.clocks[1].transition_without_reset(60):
            self.dash_image = self.dash_sprites[1]

        elif player_instance.clocks[1].transition_without_reset(0):
            self.dash_image = self.dash_sprites[0]

    # draws all the icons
    def draw(self, canvas):

        #Pistol
        canvas.draw_image(self.pistol_image, (self.dims[0] // 2, self.dims[1] // 2),
                          self.dims, self.position, (self.dims[0] / 8, self.dims[1] / 8),
                         0)
        #Sword
        canvas.draw_image(self.sword_image, (self.dims[0] // 2, self.dims[1] // 2),
                          self.dims, self.position1, (self.dims[0] / 8, self.dims[1] / 8),
                         0)

        #Dash
        canvas.draw_image(self.dash_image, (self.dims[0] // 2, self.dims[1] // 2),
                          self.dims, self.position2, (self.dims[0] / 8, self.dims[1] / 8),
                          0)

