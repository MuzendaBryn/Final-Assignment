import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def total_area(shapes):
    return sum(shape.area() for shape in shapes)


# Example usage
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
print(f"Total area of all shapes: {total_area(shapes):.2f}")
