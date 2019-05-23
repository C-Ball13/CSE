world_map = {}


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, up=None, down=None,
                 character=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.character = character


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
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
    print("You got hit bad some of your durability is gone.")


class Neck(Armor):
    def __init__(self):
        super(Neck, self).__init__("Head", 120)


class Shoulder(Armor):
    def __init__(self):
        super(Shoulder, self).__init__("Shoulder", 150)


class Back(Armor):
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


class Waist(Armor):
    def __init__(self):
        super(Waist, self).__init__("Waist", 150)


class Legs (Armor):
    def __init__(self):
        super(Legs, self).__init__("Legs", 150)


class Feet(Armor):
    def __init__(self):
        super(Feet, self).__init__("Feet", 150)


class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage:
            print("No damage is done because of some armor.")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


sword = Weapon("Sword", 32)
knife = Weapon("knife", 42)
longbow = Weapon("longbow", 50)
Polearm = Weapon("Polearm", 50)
Spears = Weapon("Spears", 42)
AssaultShotgun = Weapon("AssaultShotgun", 50)
Axe = Weapon("Axe", 30)
PumpShotgun = Weapon("PumpShotgun", 50)
AssaultRifle = Weapon("AssaultRifle", 50)
SMG = Weapon("SMG", 32)
XR2 = Weapon("XR2", 50)


Toni_Armor = Armor("Armor of the gods", 50)


orc = Character("Orc1", 50, sword, Toni_Armor)
orc2 = Character("Orc2", 50, knife, Toni_Armor)
orc3 = Character("Orc3", 50, longbow, Toni_Armor)
orc4 = Character("Orc4", 50, Polearm, Toni_Armor)
orc5 = Character("Orc5", 50, Spears, Toni_Armor)
orc6 = Character("Orc6", 50, AssaultShotgun, Toni_Armor)
orc7 = Character("Orc7", 50, Axe, Toni_Armor)
orc8 = Character("Orc8", 50, PumpShotgun, Toni_Armor)
orc9 = Character("Orc9", 50, AssaultRifle, Toni_Armor)
orc10 = Character("Orc10", 50, SMG, Toni_Armor)
orc11 = Character("Orc11", 50, XR2, Toni_Armor)

orc.attack(orc2)
orc2.attack(orc3)
orc3.attack(orc4)
orc4.attack(orc5)
orc5.attack(orc6)
orc6.attack(orc7)
orc7.attack(orc8)
orc8.attack(orc9)
orc9.attack(orc10)
orc10.attack(orc11)
orc11.attack(orc)


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room
        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that direction.
        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


Place_Unknown_Nuketown = Room("Nuketown Blue House", "This is where you are now ", None, None, "Looped_Road", None,
                              None, None, None)
Looped_Road = Room("WestSide of looped Road", "There some word on the wall but its unreadable "
                                              "and helmet next to it", None,
                   None, "Nuketown_Yellow_House", "Place_Unknown_Nuketown", None, None, [orc])
Nuketown_Yellow_House = Room("Nuketown Yellow House", "there's an chest plate on the couch and dead body next to it.",
                             None, None, "Nuketown_Kitchen", "Looped_Road", None, None, None)
Nuketown_Kitchen = Room("Yellow House Kitchen", "There's an orc eating food and in your vision there's an gun XR2",
                        None, None, None, None, "Nuketown_Yellow_House", "Attic", [orc2])
Attic = Room("Yellow House Attic", "there's two orc in here ready to kill you better think fast. ", None, None, None,
             None, "Nuketown_Kitchen", "Watermelon_Attic",[orc3])
Watermelon_Attic = Room("Attic", "this is an bigger attic and there some weapon and leggings as armor ", None, None,
                        None, None, "Attic", "Attic_Stairs", None)
Attic_Stairs = Room("Attic Stairs", "there's an orc on theses stairs kill him now", None, None, "East_Side_attic",
                    "Watermelon_Attic", None, None, [orc4])
East_Side_attic = Room("East-Side Attic", "There some boots on the floor and back plate and "
                                          "be careful orc be popping out", None, None, None, None, "East_Side_attic",
                       "Rest_Room", [orc5])
Rest_Room = Room("Rest Room", "there's some wrists guards that boost your health ", "Attic_Hallway", None, None, None,
                 "East_Side_attic", None, None)
Attic_Hallway = Room("Attic_Hallway", "there's an orc that look bigger than all the other one's "
                                      "this should take longer than the other ones", None, "Rest_Room",
                     None, "GBO_Game_Room", None, None, [orc6])
GBO_Game_Room = Room("G-BO Game-Room", "there's Longbow,Polearm,Spears,and Sword",
                     None, None, "Attic_Hallway", "West_Side_Attic", None, None, None)
West_Side_Attic = Room("West-Side Attic", "an light on the wall started to glow and it says an enemy is near",
                       None, None, "GBO_Game_Room", "Quad_Studios", None, None, [orc7]),
Quad_Studios = Room("Quad Studios", "there's clippers on the floor and 2 orcs in here", None, "hp_Afro_Repair",
                    "West_Side_Attic", None, None, None, [orc8, orc9])
hp_Afro_Repair = Room("hp Afro Repair", "an light turn on and says grab 2 thing only. There's MarksmanRifle,"
                                        "AssaultShotgun,Axe,and SMG", "Quad_Studios", None, "Cafe", None, None, None)
Cafe = Room("Cafeteria", "you should put and necklaces and some shoulder blades on "
                         "that's on the wall because there's an boos you have to kill ",
            None, None, None, "hp_Afro_Repair", None, None, [orc10])
player = Player(Place_Unknown_Nuketown)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
command = ''

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    elif command.lower()[0:4]== "take":
        command1 = command.lower().split()
        thing = "" "".join(command1[1:])
        try:
            grab= False
            for i in range(len(player.current_location.item)):
                if player.current_location.item[i - 1].name.lower() == thing.lower():
                    itemindex = i - 1
                    if issubclass(type(player.current_location.item[itemindex]), Weapon)is True:
                        if player.weapon is None:
                            player.weapon = player.current_location.item[itemindex]
                        else:
                            print("you drop your %s." % player.weapon.name)
                            very = player.weapon
                            player.weapon = player.current_location.item[itemindex]
                            player.current_location.item.append (very)
                            player.inventory.remove(very)
                    player.inventory.insert(0,player.current_location.item[itemindex])
                    print(player.current_location.item[itemindex].name + "has been added to your inventory")
                    player.current_location.item.pop.(itemindex)
                    grabbed = True
                    
    else:
        print("Command not recognized.")

