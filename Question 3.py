class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass  # Base class method does nothing


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")  # Calls the Shape class constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        super().calculate_area()  # Calls the base method, even though it's empty
        return self.width * self.height


# Example usage
rect = Rectangle(4, 5)
print(f"{rect.name} area: {rect.calculate_area()}")  # Output: Rectangle area: 20
