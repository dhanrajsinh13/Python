# SORTING IN PYTHON .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects

fruits = ["banana", "orange", "apple", "coconut", "mango"]
fruits1 = ("banana", "orange", "apple", "coconut", "mango")
fruits2 = {"banana": 105,
           "orange": 73,
           "apple": 72,
           "coconut": 354,
           "mango": 133}

fruits.sort(reverse=True)
fruits1 = tuple(sorted(fruits1, reverse=True))
# fruits2 = dict (sorted(fruits2.items(), reverse=True)
# fruits2 = dict (sorted(fruits.items(), key=lambda item: item[0], reverse=True))
# fruits2 = dict (sorted(fruits.items(), key=lambda item: item[1]))
fruits2 = dict (sorted(fruits2.items(), key=lambda item: item[1], reverse=True))

print(fruits)
print(fruits1)
print(fruits2)

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name} ({self.calories} calories)"

fruits = [Fruit("banana", 105),
              Fruit("apple", 72),
              Fruit("orange", 73),
              Fruit("coconut", 354)]

fruits = sorted(fruits, key=lambda fruit: fruit.name)

print(fruits)
