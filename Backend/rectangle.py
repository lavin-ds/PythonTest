from shape import Shape

class Rectangle(Shape):
    "Rectangle"
    # constructor
    def __init__(self, breadth, length, colour):
        super().__init__(colour)
        self.breadth = length
        self.length = length


    def area(self):
        "area of a rectangle"
        return self.length * self.breadth
    
