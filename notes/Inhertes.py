class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.milage = milage

    def start_engine (self):
        self.engine_status = True
        print("You turn the key and the car turns on")

    def move_forward(self):
        self.fuel -= 1
        print("The car move forward")

    def turn_left(self):
        self.fuel -= 1
        print("The car turn left")

    def turn_off(self):
        self.engine_status = False
        print("You turn off the car ")


class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__("Impala", 25)


class KeylessCar(Car):
    def __init__(self, name, milage):
        super(KeylessCar, self).__init__(name , milage)


caleb_car = Impala
caleb_car.start_engine()
caleb_car.move_forward()
caleb_car.turn_left()
caleb_car.move_forward()
caleb_car.turn_left()



