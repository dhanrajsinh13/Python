
fruits = ["Apple", "Orange", "Banana", "Coconut"]
vegetables = ["Celery", "Carrots", "Potatoes"]
meats = ["Chicken", "Fish", "Turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0])
print(groceries[1])
print(groceries[0][1])
# print(groceries[1][0])
# print(groceries[2][2])
print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()