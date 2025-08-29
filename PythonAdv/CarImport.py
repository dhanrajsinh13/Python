class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale =for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

    def desc(self):
        print(f"{self.model} {self.color} {self.year}")

car1 = Car("Toyota Camry", 2022, "Blue", True)
print(car1.drive())
print(car1.stop())
print(car1.desc())