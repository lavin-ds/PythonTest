import unittest
from circle import Circle
from square import Square

class ShapesTest(unittest.TestCase):
    def test_area_of_circle(self):
        # Arrange
        circle = Circle(5)

        # Act
        result = circle.area()

        # Assert
        self.assertEqual(result, 11)

    def test_properties_of_square(self):
        # Arrange
        square = Square("blue", 3)

        # Act
        result = square.area()

        # Assert
        self.assertEqual(result, 30)
        self.assertEqual(square._colour, "blue")

    # def test_properties_of_rectangle(self):
    #     # Arrange

    #     # Act

    #     # Assert
    