
unit = input("Is this temperature in celsius or fahrenheit (C/F): ")
temp = float(input("Enter the temperature :"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32,1)
    print(f"The temperature in fahrenheit : {temp}°F")
elif unit == "F":
    temp = round((temp - 32)* 5 / 9,1)
    print(f"The temperature in Celsius : {temp}°C")
else :
    print(f"{unit} was not valid.")

