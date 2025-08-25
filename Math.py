import math

friend=10

friend +=1
print(friend)
friend -=1
print(friend)
friend *=3
print(friend)
friend /=3
print(friend)
friend **=2
print(friend)
remainder = friend %2
print(remainder)
print()

x=10.5
print(math.pi)
print(math.e)
print(math.sqrt(x))
print(math.ceil(x))
print(math.floor(x))
print()

radius = float(input("Enter the radius of circle: "))
circumfrence =2 * math.pi * radius
area = math.pi * pow(radius,2)
print(f"the circumfrence is : {round(circumfrence,2)}cm")
print(f"the area of circle is : {area}cm^2")
print()

a =float(input("Enter side A: "))
b =float(input("Enter side B: "))
print(f"Side c ={math.sqrt(pow(a,2)+pow(b,2))}")