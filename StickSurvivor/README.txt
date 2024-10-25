STICK SURVIVOR (Uni project from year 1)

RQUIREMENTS
Ensure Python and SimpleGUICS2Pygame.simpleguics2pygame are installed on your system.
To install SimpleGUICS2Pygame.simpleguics2pygame, execute the following terminal command:

$ python -m pip install SimpleGUICS2Pygame --user
For more detailed instructions, visit: SimpleGUICS2Pygame PyPI

PLAYING THE GAME
To initiate the game, run the main.py script:
$ python3 main.py
Upon the initial launch, enjoy a brief background story.
Please note it will only appear once.
However, if you wish to see it, adjust the value in game_data.txt back to 0.

MOVEMENT
A - Run Left, 
D - Run Right 
SPACEBAR - Jump (You need to hold it)
S - Dash (3 second cooldown)
R - Hit with Fists 
E - Shoot (3 second cooldown)
R - Hit with Sword (3 second cooldown)
P - Pause the game and get back to the game 

Use your mouse to navigate in the menus

HAVE FUN!

\
 \    O
 _\|  |  }
   M_/|\_|}
      |  }
     / \
   _/   \_

ADDITIONAL INFORMATION:
-----------------------
FILES/FOLDERS:
In assets you will find all the Assets that have been used for this game.
In music you will find all the background music files and the sound effects, which have been used for this game.
This game was developed in the pycharm IDE and therefore has the automatically generated files lib/music/bin/share included as well.

Backgrounds.py contains the Backgrounds class, which sdraws and updates the Background.
Backstory.py contains the Backstory class, which draws the Backstory and has a mouse_click() function so that you can click through it.
Bullet.py contains the logic for all the bullets in the game.
Clock.py contains the Clock class which we generated objects from instead of using counters the entire time.
Damage.py contains the Damage class, which manages damages between Zombie and Player.
Deathscreen.py contains the Deathscreen class, which draws the Deathscreen and adds functionaily to the buttons with the mouse_click() function. (child of Menu class)
Floor.py draws the Floor, which the Player stands on.
game_data.txt contains the overall highscore.
GUI.py contains the GUI class, which draws and updates the icons in the top right hand corner of the screen. (The  icons indicate how long it takes to use a certain ability again)
GunZombie.py contains the GunZombie class, which is a child class of the Zombie class. It updates the GunZombies in game and the class contains the logic behind it. (when it shoots, how close it has to be to shoot ... etc)
Healthbar.py contains the Healthbar class, which indicates how many lives the player has. The class draws and updates the healthbar.
Interaction.py contains the Interaction class, which takes the keyboard input from the Keyboard class and calls the according functions in the Player class.
Keyboard.py contains the Keyboard class, which takes the keyboard input and saves it into variable. (with the help of the keyDown and keyUp functions)
main.py is the file in the game, which makes a game out of all the different classes.
MainMenu.py contains a class, which draws the MainMenu.
Menu.py contains the Menu class, which is the parent class of DeathScreen, MainMenu and Pause.
Pause.py contains the Pause class, which pauses the game and draws the pause menu.
Player.py contains the Player class, which draws the Player and updates the Player. It also contains his movement and abilities/weapons.
PowerUps.py contains the PowerUps class, which draws a PowerUp and updates it.
Score.py contains the Score class, which reads the highscore from the game_data.txt file and updates the score/highscore.
SwordZombie.py contains the SwordZombie class, which updates the GunZombie in game and it contains the logic behind it. (when it uses his sword and how close it has to be use his sword... etc)
Vector.py contains the Vector class, which we were provided with.
Zombie.py is the parent class of GunZombie and SwordZombie.


SOURCES / Credits:
White Stickman sprites      https://rgsdev.itch.io
Bullet sprite               https://rgsdev.itch.io
Forest Background           https://saurabhkgp.itch.io/pixel-art-forest-background-simple-seamless-parallax-ready-for-2d-platformer-s
Music/Soundeffects		    https://pixabay.com/music/
Fist icon                   https://uxwing.com/boxing-glove-icon/
Sword icon                  https://uxwing.com/sword-icon/
Pistol icon                 https://uxwing.com/gun-pistol-icon/
Dash icon                   https://thenounproject.com/icon/dash-5001585/

(All the other artwork has been created by our team)



