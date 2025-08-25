from operator import truediv

responce = input("Would you like food? (Y/N):")
if responce =="Y" or "y":
    print("Have some food!")
else:
    print("No food for you!")

name =input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

for_sale= True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is Not.")