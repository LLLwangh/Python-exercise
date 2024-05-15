# chapter 9 as function

class Restaurant:
    "create a restaurant class"

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served_count = 0

    def describe_restaurant(self):
        print(self.name + " restaurant is clean and luxury")

    def open_restaurant(self):
        print("This is a " + self.type + " restaurant")

    def number_served(self):
        print("There were " + str(self.number_served_count) + " have been here today.")

new_restaurant = Restaurant('Panda', 'beef')
new_restaurant.number_served_count = 3
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
new_restaurant.number_served()

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odmeter(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot rollback.")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('Tesla','Model Y', 2024)
print(my_tesla.get_descriptive_name())

    


