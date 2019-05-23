world_map = {}


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None,west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.character = []


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
                              None, None)
Looped_Road = Room("WestSide of looped Road", "There's an letter on the floor and helmet next to it", None, None,
                   "Nuketown_Yellow_House", "Place_Unknown_Nuketown", None, None)
Nuketown_Yellow_House = Room("Nuketown Yellow House", "there's an chest plate on the couch and dead body next to it.",
                             None, None, "Nuketown_Kitchen", "Looped_Road", None, None)
Nuketown_Kitchen = Room("Yellow House Kitchen", "There's an orc eating food and in your vision there's an gun XR2",
                        None,None, None, None, "Nuketown_Yellow_House", "Attic")
Attic = Room("Yellow House Attic", "there's two orc in here ready to kill you better think fast. ", None, None, None,
             None, "Nuketown_Kitchen", "Watermelon_Attic")
Watermelon_Attic = Room("Attic", "this is an bigger attic and there some weapon and leggings as armor ", None, None, None, None, "Attic", "Attic_Stairs")
Attic_Stairs = Room("Attic Stairs", "there's an orc on theses stairs kill him now", None, None, "East_Side_attic",
                    "Watermelon_Attic", None, None)
East_Side_attic = Room("East-Side Attic", "There some boots on the floor and back plate and "
                                          "be careful orc be popping out", None, None, None, None, "East_Side_attic",
                       "Rest_Room")
Rest_Room = Room("Rest Room", "there's some wrists guards that boost your health ", "Attic_Hallway", None, None, None,
                 "East_Side_attic", None)
Attic_Hallway = Room("Attic_Hallway", "there's an orc that look bigger than all the other one's "
                                      "this should take longer than the other ones", None, "Rest_Room",
                     None, "GBO_Game_Room", None, None)
GBO_Game_Room = Room("G-BO Game-Room", "there's Longbow,Polearm,Spears,and Sword",
                     None, None, "Attic_Hallway", "West_Side_Attic", None, None)
West_Side_Attic = Room("West-Side Attic", "an light on the wall started to glow and it says an enemy is near",
                       None, None, "GBO_Game_Room", "Quad_Studios", None, None)
Quad_Studios = Room("Quad Studios", "there's clippers on the floor and 2 orcs in here", None, "hp_Afro_Repair",
                    "West_Side_Attic", None)
hp_Afro_Repair = Room("hp Afro Repair", "an light turn on and says grab 2 thing only. There's MarksmanRifle,"
                                        "AssaultShotgun,Axe,and SMG", "Quad_Studios", None, "Cafe", None, None, None)
Cafe = Room("Cafeteria", "you should put and necklaces and some shoulder blades on "
                         "that's on the wall because there's an boos you have to kill ",
            None, None, None, "hp_Afro_Repair", None, None)
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
    else:
        print("Command not recognized.")


while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")

