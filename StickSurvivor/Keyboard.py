try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui



class Keyboard:

    # Constructor
    def __init__(self):
        self.right = False
        self.left = False
        self.space = False
        self.s_key = False
        self.q_key = False
        self.e_key = False
        self.r_key = False

    # checks if keys are pressed and while they are pressed down it sets the according key variable to true (otherwise to false)
    def keyDown(self, key):

        if key == simplegui.KEY_MAP["s"]:  # Check for "s" key
            self.s_key = True
        elif key == simplegui.KEY_MAP["right"]:
            self.right = True
        elif key == simplegui.KEY_MAP["left"]:
            self.left = True
        elif key == simplegui.KEY_MAP["a"]:
            self.left = True
        elif key == simplegui.KEY_MAP["d"]:
            self.right = True
        elif key == simplegui.KEY_MAP["space"]:
            self.space = True
        elif key == simplegui.KEY_MAP["q"]:
            self.q_key = True
        elif key == simplegui.KEY_MAP["e"]:
            self.e_key = True
        elif key == simplegui.KEY_MAP["r"]:
            self.r_key = True
    def keyUp(self, key):

            if key == simplegui.KEY_MAP["s"]:  # Check for "s" key
                self.s_key = False
            elif key == simplegui.KEY_MAP['right']:
                self.right = False
            elif key == simplegui.KEY_MAP["left"]:
                self.left = False
            elif key == simplegui.KEY_MAP["a"]:
                self.left = False
            elif key == simplegui.KEY_MAP["d"]:
                self.right = False
            elif key == simplegui.KEY_MAP["space"]:
                self.space = False
            elif key == simplegui.KEY_MAP["s"]:  # Check for "s" key
                self.s_key = False
            elif key == simplegui.KEY_MAP["q"]:
                self.q_key = False
            elif key == simplegui.KEY_MAP["e"]:
                self.e_key = False
            elif key == simplegui.KEY_MAP["r"]:
                self.r_key = False
