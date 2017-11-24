class Vehicle:
    pass
class Truck(Vehicle):
    pass
print(isinstance(Vehicle(),Vehicle))
print(type(Vehicle())==Vehicle)

print(isinstance(Truck(),Vehicle))
print(type(Truck())==Vehicle)
