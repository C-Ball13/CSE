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
        super(XR2, self).__init__("XR2", 70)


class SMG(Weapon):
    def __init__(self):
        super(SMG, self).__init__("SMG", 60)


class AssaultRifle(Weapon):
    def __init__(self):
        super(AssaultRifle, self).__init__("AssaultRifle", 90)


class PumpShotgun(Weapon):
    def __init__(self):
        super(PumpShotgun, self).__init__("PumpShotgun", 80)


class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__("Axe", 50)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword", 70)


class AssaultShotgun(Weapon):
    def __init__(self):
        super(AssaultShotgun, self).__init__("AssaultShotgun", 60)


class ICR7(Weapon):
    def __init__(self):
        super(ICR7, self).__init__("ICR7", 75)


class MarksmanRifle(Weapon):
    def __init__(self):
        super(MarksmanRifle, self).__init__("MarksmanRifle", 100)


class Glock9(Weapon):
    def __init__(self):
        super(Glock9, self).__init__("Glock9", 65)


class MetalBat(Weapon):
    def __init__(self):
        super(MetalBat, self).__init__("MetalBat", 95)


class FighingKnife(Weapon):
    def __init__(self):
        super(FighingKnife, self).__init__("FightingKnife", 45)


class Spears(Weapon):
    def __init__(self):
        super(Spears, self).__init__("Spears", 35)


class Polearm (Weapon):
    def __init__(self):
        super(Polearm, self).__init__("Polearm", 55)


class Longbow (Weapon):
    def __init__(self):
        super(Longbow, self).__init__("Longbow", 55)


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


def got_hit(self):
    self.durability -= 10
    print("You got hit bad some of your durability")


class Head(Armor):
    def __int__(self):
        super(Head, self).__init__("Head", 150)


class Neck(Armor):
    def __init__(self):
        super(Neck, self).__init__("Head", 120)


class Shoulder(Armor):
    def __init__(self):
        super(Shoulder, self).__init__("Shoulder", 150)


class Back(Item):
    def __init__(self):
        super(Back, self).__init__("Back", 120)


class Chest(Armor):
    def __init__(self):
        super(Chest, self).__init__("Chest", 150)


class Wrists(Armor):
    def __init__(self):
        super(Wrists, self).__init__("Wrists", 130)


class Hands(Armor):
    def __init__(self):
        super(Hands, self).__init__("Hands", 150)

