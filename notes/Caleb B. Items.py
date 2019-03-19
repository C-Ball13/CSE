class Item(object):
    def __init__(self,name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_ant):
        super(Armor, self).__init__(name)
        self.armor_ant = armor_ant