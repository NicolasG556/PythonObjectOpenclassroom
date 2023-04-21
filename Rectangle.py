class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    def calculerSurface(self):
        return self.length * self.width


rectangle = Rectangle(5, 3)

print(rectangle.length)
rectangle.color = "yellow"

area = rectangle.calculerSurface()
print(area)