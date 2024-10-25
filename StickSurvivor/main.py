from Score import Score

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Player import Player
from Keyboard import Keyboard
from Interaction import Interaction
from Floor import Floor
from Clock import Clock
from GUI import GUI
from Pause import PauseMenu
from Backgrounds import Backgrounds
from SwordZombie import SwordZombie
from GunZombie import GunZombie
from Damage import Damage
from DeathScreen import DeathScreen
from PowerUps import PowerUp
from MainMenu import MainMenu
import random
from BackStory import BackStory

sounds_on = True

# frame width and height
width = 800
height = 600


# Ground
Ground = 500
constant = 65

# make player_instance object from Player class
player_instance = Player((200, Ground - constant),
                         8, ##Playerspeed
                         200,### Jumpspeed
                         )

# Create frame
frame = simplegui.create_frame("Stick Survivor", width, height)
frame.set_canvas_background("white")

# create objects of Keyboard and Interaction class
kbd = Keyboard()
inter = Interaction(player_instance, kbd)

# initilaize gui object from GUI class
gui = GUI()

# Background
background = Backgrounds(width, height)
background_change = False
background_counter = Clock()
background_counter.start()
background_sprite_counter = 0

# PowerUp
y1 = 100
y2 = 300
powerup = PowerUp(width, height, 150, 150, y1, y2)

# Score
score = Score()
score_c = Clock()       # used for updating the score every second
score_c.start()


# Waves
wave_number = 1
miniwave_number = 1
zombies = []
Wave_counter = Clock()
Wave_counter.start()
Miniwave_counter = Clock()
Miniwave_counter.start()

# Deathscreen
deathscreen_counter = Clock()
deathscreen_counter.start()

# MainMenu
mainmenu = MainMenu(width, height, score.score, score.highscore)

# Backstory
if score.highscore == 0:
    bs = BackStory(width, height)

#game music
game_music = simplegui._load_local_sound("music/Background_music/Hitman(chosic.com).mp3")

game_music_counter = Clock()
game_music_counter.start()

# Music - not available yet
#music_off = False
#soundeffects_off = False


start = True # for backstory important
game_ended = False

# the game is in here
def game_start(canvas):
    global background_counter, background_sprite_counter, game_ended, background_change, wave_number, miniwave_number


    # check if game has not already ended and the background has not been changed
    if not game_ended and not background_change:

        # check if player is dead
        if player_instance.health <= 0:
            deathscreen_counter.tick()
        # check if it is after 3 seconds of the player being dead
        if deathscreen_counter.transition(180):
            game_ended = True

        # update clocks
        Wave_counter.tick()
        Miniwave_counter.tick()
        background_counter.tick()
        score_c.tick()

        # background changes every 20 seconds (every wave)
        if background_counter.transition(60 * 20):
            background_change = True

        if score_c.transition(60):
            score.update_score_second()

        # increase the wave number every 20 seconds -> every 20 seconds new wave
        if(Wave_counter.transition(60 * 20)): # Wave
            wave_number += 1

        # increase the miniwave number every 5 seconds and set it to 0 when it is 5
        if Miniwave_counter.transition(60 * 5):
            if miniwave_number == 5:
                miniwave_number = 0

            if wave_number % 2 == 0: # even number
                if miniwave_number == 3:
                    spawn_zombie(number=wave_number - 1)
                else:
                    spawn_zombie(number=wave_number)

            else:                    # odd number
                if miniwave_number == 3:
                    spawn_zombie(number=wave_number + 1)
                else:
                    spawn_zombie(number=wave_number)

            miniwave_number += 1

        # draw the background, score and player_instance
        background.draw(canvas)
        score.draw(canvas, 32, "White")
        player_instance.draw(canvas)

        # check if player is alive and if so update the Interaction class
        # User shouldn't be able to move while being dead
        if player_instance.health > 0:
            inter.update()

        # updates and draws powerup
        powerup.update()
        powerup.draw(canvas)
        if powerup.active:
            player_size = (512/2, 512/2)
            if powerup.collision(player_instance.position, player_size):
                powerup.active = False
                if player_instance.health < 3:
                    player_instance.health += 1


        # draw Floor
        F1 = Floor((0, Ground), (width, Ground), 10)
        F1.draw(canvas)

        # update all clocks from playerobject
        for clock in player_instance.clocks:
            clock.tick()
        # update and draw all zombies from zombies list
        for zombie in zombies:
            zombie.update(player_instance.position)
            zombie.draw(canvas)

            d1 = Damage(player_instance, zombie)
            # update player and zombie health
            player_instance.health = player_instance.health - d1.makes_damage()
            zombie.health = zombie.health - d1.damage_from_player()

            # remove zombie from the list that is getting updated and update score (-> zombie kill is 5 points)
            if zombie.health <= 0:
                zombies.remove(zombie)
                score.update_score_kill()

        # update and draw gui
        gui.update(player_instance)
        gui.draw(canvas)

    # background update animation (white flash for 1/3 second)
    if background_change:
        background_counter.tick()
        if background_counter.transition(20):
            background_sprite_counter += 1
            if background_sprite_counter == 3:
                background_sprite_counter = 0
            background.change_background(background_sprite_counter)
            background_change = False

# reset all the variables in the game (-> so that the player can play another round)
def reset_game():
    global game_ended, player_instance, zombies, score, score_c, background_change, background_counter, background_sprite_counter, inter, kbd
    global wave_number, miniwave_number
    game_ended = False
    player_instance = Player((200, Ground - constant), 8, 200)
    zombies.clear()
    score.reset_score()
    score_c.reset()
    background_change = False
    background_counter.reset()
    background_sprite_counter = 0
    inter = Interaction(player_instance, kbd)
    wave_number = 1
    miniwave_number = 1

# gets updated every frame (60 frames every second)
def draw(canvas):
    global start, game_ended

    # User has played the game before (his/her highscore is not 0)
    if score.highscore != 0 or bs.done:
        # main menu
        if start:
            # rewind and pause other music
            game_music.rewind()
            game_music.pause()
            death_screen.menu_music.rewind()
            death_screen.menu_music.pause()

            # play main menu music
            mainmenu.menu_music.play()
            mainmenu.draw(canvas)
            # set the mouseclick_handler for the frame to mainmenu mousclick
            frame.set_mouseclick_handler(mainmenu.mouse_click)

            # update the score for mainmenu and pause
            mainmenu.update_scores(score.score, score.highscore)

            # if play button is pressed --> user wants to play a game
            if mainmenu.play_button_pressed:
                start = False
                mainmenu.reset()
                reset_game()
                game_ended = False
                score.update_highscore()

        # Game
        elif game_ended == False:
            # rewind and pause other music
            mainmenu.menu_music.rewind()
            mainmenu.menu_music.pause()
            death_screen.menu_music.rewind()
            death_screen.menu_music.pause()

            pause.update_scores(score.score, score.highscore)

            # set the mouseclick_handler for the frame to pause mouseclick
            frame.set_mouseclick_handler(pause.mouse_click)

            # if user presses the menu button
            if pause.menu_button_pressed:
                start = True
                pause.reset()
                game_ended = True

            # if game is not paused
            if not pause.paused:
                game_music.play()
                game_start(canvas)

        # Deathscreen
        elif game_ended == True:
            # rewind and pause other music
            game_music.rewind()
            game_music.pause()
            mainmenu.menu_music.rewind()
            mainmenu.menu_music.pause()

            # after death highscore gets updated
            score.update_highscore()
            # play deathscreen music
            death_screen.menu_music.play()
            # update and draw death_screen
            death_screen.update_scores(score.score, score.highscore)
            death_screen.draw(canvas)
            # set the mouseclick_handler for the frame to death screen mouseclick
            frame.set_mouseclick_handler(death_screen.mouse_click)

            # if the user presses the play button on the deathscreen
            if death_screen.play_button_pressed:
                death_screen.reset()
                reset_game()
                game_ended = False
                score.update_highscore()

            # if the user presses the menu button on the deathscreen
            if death_screen.menu_button_pressed:
                death_screen.reset()
                start = True

    # User has never played the game before (his highscore is 0) -> Background story
    else:
        frame.set_mouseclick_handler(bs.mouse_click)
        bs.draw(canvas)


# spawn a number of zombies and append them to the zombies list
def spawn_zombie(number):
    for x in range(number):
        global zombies
        # randomized if GunZombie or SwordZombie zombie
        r = random.randint(0, 1)
        if r == 1:
            zombies.append(GunZombie((800 + 100 + x * 20, 435)))
        else:
            zombies.append(SwordZombie((800 + 100 + x * 20, 435)))

# key_handler - for the pause button "p"
def key_handler(key):

    global game_ended, start

    # check if the user is in the game and not in the menu
    if not game_ended and not start:
        pause.toggle_pause(key)
        game_music.pause()
        if not pause.paused:
            kbd.keyDown(key)

# Menus
pause = PauseMenu(frame, draw,  width, height, score.score,  score.highscore)
death_screen = DeathScreen(width, height, score.score,  score.highscore)

# set handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_keydown_handler(key_handler)

# Start the frame animation
frame.start()
