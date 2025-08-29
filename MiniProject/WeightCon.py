
weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds (K or l): ")

if unit == "K" or "Kilograms":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L" or "Pounds":
    weight = weight / 2.205
    unit = "Kgs."
else :
    print(f"{unit} was not valid.")

print(f"Your weight is: {weight} {unit}")




