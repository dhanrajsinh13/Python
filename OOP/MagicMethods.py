# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.num_pages == other.num_pages

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return None

book1 = Book("Harry Potter...", "J.K. Rowling", 234)
book2 = Book("The Hobbit", "J. R. R. Tolkein", 345)
book3 = Book("The Colour Of Magic", "Terry Practchet", 456)

print(book1)
print(book2 == book3)
print(book2 < book3)
print(book3 > book1)
print(book1 + book2)
print("Harry" in book1)
print(book1['author'])