try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


import random

class PowerUp:
    # Constructor
    def __init__(self, game_width, game_height, width, height, y1, y2):
        self.game_width = game_width
        self.game_height = game_height
        self.width = width
        self.height = height
        self.y1 = y1
        self.y2 = y2
        self.active = False
        self.images = [simplegui._load_local_image(f"Assets/PowerUp/Test{i}.png") for i in range(1, 5)]
        self.frame_index = 0
        self.count = 0
        self.active_time = 0
        self.cooldown = 0
        self.random_pos()
        self.sound = simplegui._load_local_sound("music/health-pickup-6860.mp3")

    # calculates a random position
    def random_pos(self):
        self.x = random.randint(0, self.game_width - self.width)
        self.y = random.randint(self.y1, self.y2)


    # handels when it can spawn and its animation
    def update(self):
        # spawns powerup after at least 3 seconds to the last one and if there is not already one and random component
        if not self.active and self.cooldown == 0 and random.random() < 0.001:
            self.active = True
            self.active_time = 0
            self.random_pos()

        # animation
        if self.active:
            self.count += 1
            self.active_time += 1

            if self.count % 20 == 0:
                self.frame_index = (self.frame_index + 1) % len(self.images)
                self.count = 0

            if self.active_time >= 200:
                self.active = False
                self.cooldown = 180

        elif self.cooldown > 0:
            self.cooldown -= 1

    # draws powerup (if active)
    def draw(self, canvas):
        if self.active:
            current_image = self.images[self.frame_index]
            image_center = (current_image.get_width() / 2, current_image.get_height() / 2)
            image_size = (current_image.get_width(), current_image.get_height())
            canvas.draw_image(current_image, image_center, image_size, (self.x + self.width / 2, self.y + self.height / 2), (self.width, self.height))

    # checks collision between player and powerup - returns true if collision detected and false if not
    def collision(self, player_position, player_size):
        player_x, player_y = player_position.x, player_position.y
        player_width, player_height = player_size

        if (self.x < player_x + player_width and
            self.x + self.width > player_x and
            self.y < player_y + player_height and
            self.y + self.height > player_y):
            self.sound.play()

            return True
        return False
