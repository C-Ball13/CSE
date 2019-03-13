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
caleb_car.start_engine(),
caleb_car.move_forward(),
caleb_car.turn_left(),
caleb_car.move_forward(),
caleb_car.turn_left()


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self,name,damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, damage):
        super(Armor, self).__init__(name)
        self.armor_ant = armor_ant


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor


sword = Weapon("Sword, 10")
canoe = Weapon("Canoe", 42)


orc = Character("Orcl", 100, sword, Armor(Genertic))