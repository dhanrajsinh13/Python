# dictionary =  a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals= {"USA": "Washington D.C.",
           "India": "New Delhi",
           "China": "Beijing",
           "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.pop("China")
keys = capitals.keys()
print(capitals)
print(keys)