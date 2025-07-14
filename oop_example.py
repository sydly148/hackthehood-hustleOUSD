class Car:
    def __init__(self, model, color, make, year, size, mileage, top_speed, height):
        '''Defines all of the attributes of a car object.'''
        self.model = model
        self.color = color
        self.make = make
        self.year = year
        self.size = size
        self.mileage = mileage
        self.top_speed = top_speed
        self.height = height
        self.speed = 0
        self.doors = 4
        self.open_doors = 0
    
    def open_door(self):
        '''Opens the doors of a car as long as not all 4 doors are already open.'''
        if self.open_doors < self.doors:
            self.open_doors += 1
            print(f"The door of the {self.make} {self.model} is now open.")
        else:
            print(f"All of the doors of the car are already open.")
    
    def accelerate(self, accelerator):
        '''Accelerates the speed of the car as long as it's not already at the top speed.'''
        if self.speed <= self.top_speed and (self.speed + accelerator) <= self.top_speed:
            self.speed += accelerator
            print(f"The {self.make} {self.model} accelerates to {self.speed} mph.")
        elif self.speed != self.top_speed and (self.speed + accelerator) > self.top_speed:
            self.speed = 200
            print(f"The {self.make} {self.model} accelerates to {self.speed} mph.")
        else:
            print(f"The car is already at top speed! It can't go any faster.")

    def steer(self, direction):
        '''Steers the car in a valid direction.'''
        if direction.lower() == "left" or direction.lower() == 'right':
            print(f"The {self.make} {self.model} is turning {direction}.")
        else:
            print(f"{direction} is not a valid direction. Please enter a valid direction.")

my_car = Car("Camaro", "Blue", "Chevrolet", 2016, 20, 10000, 200, 7)

