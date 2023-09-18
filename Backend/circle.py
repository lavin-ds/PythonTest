from shape import Shape

class Circle(Shape):
    "This is a circle class"
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        "Area of a circle"
        return 3.14159265359 * self.radius ** 2
    