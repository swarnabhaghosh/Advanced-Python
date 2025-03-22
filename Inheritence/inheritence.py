#inheritence is basically the child class can access the methods and attributes of the parent class.
#It helps in code reusability and establishing a relationship between classes.

class vehicle:
        def general_usage(self):
                print("general use : transportation")

class car(vehicle):
        def __init__(self):
                print("I'm a car")
                self.wheels=4
                self.has_roof=True
        def specific_usage(self):
                print("specific use : commute to work, vaccation with family")

class bike(vehicle):
        def __init__(self):
                print("I'm a bike")
                self.wheels=2
                self.has_roof=False
        def specific_usage(self):
                print("specific use : road trip, racing")

c=car()
c.general_usage()
c.specific_usage()
print(c.wheels)
print(c.has_roof)
print()
b=bike()
b.general_usage()
b.specific_usage()




