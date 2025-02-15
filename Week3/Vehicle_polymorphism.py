class Vehicle:
    def __init__(self,plate_no):
        self.plate_no = plate_no
    def descibe(self):
        print(f"It's  {self.plate_no}")

class Car(Vehicle):
    def __init__(self, plate_no,door_count):
        super().__init__(plate_no)
        self.door_count = door_count
    def num_doors(self):
        print(f"Number of doors are {self.door_count}")
    def descibe(self):
        print(f"This is a car called {self.plate_no}")
        
class Bike(Vehicle):
    pass

vehicle = Vehicle(plate_no="aa12334")
vehicle.descibe()

car = Car(plate_no="aa335364",door_count="4")
car.descibe()
car.door_count()
bike = Bike(plate_no="zz2334")
bike.descibe()
