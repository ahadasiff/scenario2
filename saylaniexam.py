# scenario 2 oop and inheritance
class Vehicle:  #define class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

    def drive(self):
        print("Car is driving.")

class Truck(Vehicle):
    def __init__(self, make, model, year, payload):
        super().__init__(make, model, year)
        self.payload = payload

    def display_info(self):
        super().display_info()
        print(f"Payload capacity: {self.payload} tons")

    def load_cargo(self):
        print("Cargo loaded onto the truck.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.num_wheels}")

    def wheelie(self):
        print("Motorcycle is doing a wheelie!")

car = Car("Toyota", "Camry", 2022, 4)
car.display_info()
car.start_engine()
car.drive()

truck = Truck("Ford", "F-150", 2020, 2.5)
truck.display_info()
truck.start_engine()
truck.load_cargo()

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 2)
motorcycle.display_info()
motorcycle.start_engine()
motorcycle.wheelie()












