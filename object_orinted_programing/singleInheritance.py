class Vehicle:
    company ="xyz"
    def __init__(self, n_wheels, n_seat, milage):
        print("init of vichele")
        self.n_wheels = n_wheels
        self.n_seat = n_seat
        self.milage = milage


    def get_details(self):
        return f"This vichel has {self.n_wheels} wheels, {self.n_seat} seats and provide and milage of{self.milage}"
v= Vehicle(4,7,20)
print(v.get_details())

class Car(Vehicle):
    model ="ABC"
    def __init__(self,car_type,drivr_type, wheels, seats, milage):
        print("Init of Car")
        self.car_type = car_type
        self.drive_type=drivr_type
        super().__init__(wheels,seats, milage)
#Car class inherit the Michel class
#Car class is called child class?derived class
#Vichel class called parent class ?base class
c1=Car("suv","manual",4,7,12)
print(c1.model)
print(c1.company)
print(c1.milage)
print(c1.get_details())
print(c1. __dict__)



