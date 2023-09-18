from shape import Shape

class Square(Shape):
    "This class is a square"
    def __init__(self, colour, side):
        super().__init__(colour)
        self.side = side

    def area(self):
        "area of a square"
        return self.side * 10
    