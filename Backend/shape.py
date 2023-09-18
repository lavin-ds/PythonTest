class Shape:
    "shape"
    def __init__(self, colour):
        self._colour = "colourless"

    def print_colour(self):
        "prints the colour of a given shape"
        print('This is a shape and its colour is - ' + self._colour)
