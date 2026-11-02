class Vehicle:
    def __init__(self, color):
        self.color = color

    def start (self):
        print("Vehicle is Starting ....")

class Car(Vehicle):
    def __init__(self, color, num_doors):
        super().__init__(color)
        self.num_doors = num_doors

    def drive(self):
        print(f"Car with{self.num_doors} doors is driving ...")

my_car = Car("Blue", 4)
my_car.start()
my_car.drive()