try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui



class Score:
    # Constructor
    def __init__(self):

        # reads first line from game_data.txt file in order to fetch the highscore
        # the highscore doesn't get reset like a normal highscore variable after every session

        with open("game_data.txt") as file:
            line = file.readline()

        if line.strip():
            self.highscore = int(line)
        else:
            self.highscore = 0

        # in the beginning of every session the score is 0
        self.score = 0



    def update_highscore(self): # called after died, death_screen

        # check if new high score was achieved
        if self.score > self.highscore:
            # sets the current score as the highscore
            self.highscore = self.score
            # overwrites old highscore in the game_data.txt file
            with open("game_data.txt", "w") as file:
                file.write(str(self.highscore))

    # Scoresystem:
    # every second is 1 point and every zombie is 20 points
    def update_score_second(self):
        self.score += 1
    def update_score_kill(self):
        self.score += 20

    # draws the Score on the top left hand corner of the screen
    def draw(self, canvas, size, color):
        format = 'Score: ' + str(self.score)
        canvas.draw_text(format, (10,20), size, color)

    # resets score for when the user plays another round in the same session
    def reset_score(self):
        self.score = 0
