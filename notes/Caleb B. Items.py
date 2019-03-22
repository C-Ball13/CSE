class Item(object):
    def __init__(self,name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


def use_weapon(self):
    self.durablity -=10
    print("You")
class XR_2(Weapon):



class Armor(Item):
    def __init__(self, name, armor_ant):
        super(Armor, self).__init__(name)
        self.armor_ant = armor_ant

