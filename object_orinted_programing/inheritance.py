class Vehicle:
    company ="xyz"
    def __init__(self, n_wheels, n_seat, milage):
        self.n_wheels = n_wheels
        self.n_seat = n_seat
        self.milage = milage


    def get_details(self):
        return f"This vichel has {self.n_wheels} wheels, {self.n_seat} seats and provide and milage of{self.milage}"
v= Vehicle(4,7,20)
print(v.get_details())

class Car(Vehicle):
    pass
#Car class inherit the Michel class
#Car class is called child class?derived class
#Vichel class called parent class ?base class
c1 = Car(4,7,25)
print(c1.get_details())