# What is super()?:-
# super() is a built-in Python function that calls a method from a parent (super) class inside a child class.

# Why use super()?
# Avoid duplicate code — you don’t rewrite what’s already in the parent.
# Make maintenance easier — change logic in one place (parent class), and it applies everywhere.
# Support multiple inheritance — Python can figure out which parent to call using the Method Resolution Order (MRO).

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"\nIt is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()  # call Shape.describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"\nIt is a square with an area of {self.width * self.width}cm^2")
        super().describe()  # call Shape.describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"\nIt is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()  # call Shape.describe()

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

circle.describe()
square.describe()
triangle.describe()

# In short:-
# Without super() → Only the child’s version runs, and you’d lose the Shape description.
# With super() → You can extend behavior rather than replace it.

# 💡 Analogy:
# Imagine you’re making a special cake 🍰.
# Parent class = basic cake recipe.
# Child class = chocolate cake recipe.
# super() = “Use the base recipe first, then add my chocolate twist.”