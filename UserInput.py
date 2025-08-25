item =input("What item would you like to buy? : ")
price = float(input("What is price? : "))
quantity =int(input("How many would you like? : "))

total = quantity * price

print(f"You brought {quantity} X {item}/s.")
print(f"Your total is: ${round(total, 2)}")

