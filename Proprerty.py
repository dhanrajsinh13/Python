class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        if self._width is None:  # Handle deleted state
            return "Width has been deleted"
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        if self._height is None:  # Handle deleted state
            return "Height has been deleted"
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        self._width = None  # Mark as deleted instead of removing the attribute
        print("Width has been deleted")

    @height.deleter
    def height(self):
        self._height = None  # Mark as deleted instead of removing the attribute
        print("Height has been deleted")


# Example usage
rectangle = Rectangle(10, 20)

# Set width and height through the setters
rectangle.width = 15  # Works fine
rectangle.height = 25  # Works fine

# Delete width
del rectangle.width

# Access using properties
print(f"Width: {rectangle.width}")  # Custom formatting in print
print(f"Height: {rectangle.height}")
