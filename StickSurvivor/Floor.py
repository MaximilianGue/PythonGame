class Floor:

    #Constructor
    def __init__(self, start, end, thickness):

        self.start = start
        self.end = end
        self.thickness = thickness

    # draws the floor which is just a simple line
    def draw(self, canvas):
        canvas.draw_line(self.start, self.end, self.thickness, "black")


