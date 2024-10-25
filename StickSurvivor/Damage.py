try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Player import Player
from Zombie import Zombie
from GunZombie import GunZombie


class Damage:

    # Constructor
    def __init__(self, player: Player, zombie: Zombie):
        self.player = player
        self.zombie = zombie
        self.load_sounds()

    # loads sounds for when either zombie or player are hit
    def load_sounds(self):
        self.hit_by_sword_sound = simplegui._load_local_sound("music/sword-hit-7160.mp3")
        self.hit_by_bullet_sound = simplegui._load_local_sound("music/086551_bullet-hit-39845.mp3")


    # returns 1 if bullet from zombie hits player and 0 if not
    def damage_from_bullet_for_player(self) -> int:
        if self.zombie.bullet != None:

            y_difference = self.zombie.position.get_y() - self.player.position.get_y()

            if self.zombie.bullet.position.get_x() < self.player.position.get_x() + 15 and self.zombie.bullet.position.get_x() > self.player.position.get_x() and y_difference <= 10:

                self.zombie.bullet = None
                self.hit_by_bullet_sound.play()
                return 1
        return 0
    # returns 1 if sword from zombie hits player and 0 if not
    def damage_from_sword_for_player(self) -> int:
        if self.zombie.dealt_damage_with_Sword:
            self.hit_by_sword_sound.play()
            return 1
        return 0

    # calls function dependent on the type of Zombie
    def makes_damage(self) -> int:
        if isinstance(self.zombie, GunZombie):
            return self.damage_from_bullet_for_player()
        else:
            return self.damage_from_sword_for_player()


    # returns 1 if bullet from player hits zombie and 0 if not
    def damage_from_bullet_for_zombie (self) -> int:

        if self.player.bullet != None:

            if self.player.bullet.position.get_x() < self.zombie.position.get_x() + 15 and self.player.bullet.position.get_x() > self.zombie.position.get_x():

                self.player.bullet = None
                self.hit_by_bullet_sound.play()
                return 1

        return 0
    # returns 1 if sword from player hits zombie and 0 if not
    def damage_from_sword_for_zombie(self) -> int:

        if self.player.swang_sword and \
                not (self.player.position.get_x() + 50 < self.zombie.position.get_x()
                 or self.player.position.get_x() >= self.zombie.position.get_x() + 50): ## and
            self.hit_by_sword_sound.play()
            return 1
        return 0
    # returns 0.5 if fists from player hit zombie and 0 if not
    def damage_from_fists_for_zombie(self) -> int:

        if self.player.swang_fists and \
                not (self.player.position.get_x() + 50 < self.zombie.position.get_x()
                 or self.player.position.get_x() >= self.zombie.position.get_x() + 50): ## and

            return 0.5
        return 0

    # adds all the damage that the player does up and returns it
    def damage_from_player(self) -> int:

        return self.damage_from_bullet_for_zombie() + self.damage_from_sword_for_zombie() + self.damage_from_fists_for_zombie()

