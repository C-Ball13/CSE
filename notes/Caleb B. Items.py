class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name: object, damage: object) -> object:
        super(Weapon, self).__init__(name)
        self.damage = damage


def use_weapon(self):
    self.durability -= 10
    print("You used most of the gun durability")


class XR2(Weapon):
    def __init__(self):
        super(XR2, self).__init__("XR2", 10)


class SMG(Weapon):
    def __init__(self):
        super(SMG, self).__init__("SMG" , 10)


class Assault(Weapon):
    def __init__(self):
        super(Assault, self).__init__()


class Armor(Item):
    def __init__(self, name, armor_ant):
        super(Armor, self).__init__(name)
        self.armor_ant = armor_ant

