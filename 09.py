class Vehicle:
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started with a key."

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started with a button."

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started with a remote start."

def start_vehicle_engine(vehicle):
    print(vehicle.start_engine())

my_car = Car()
my_motorcycle = Motorcycle()
my_truck = Truck()

start_vehicle_engine(my_car)          
start_vehicle_engine(my_motorcycle)  
start_vehicle_engine(my_truck)        
