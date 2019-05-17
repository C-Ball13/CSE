world_map = {}


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None,west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
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


Place_Unknown_Nuketown = Room("Nuketown Blue House", "This is where you are now", None, None, "Looped_Road", None)
Looped_Road = Room("WestSide of looped Road", "", None, "Place_Unknown_Nuketown", "", "")
Nuketown_Yellow_House = Room("Nuketown Yellow House", "", None, "Looped_Road", "", "")
Nuketown_Yellow_Kitchen = Room("Yellow House Kitchen", "", None, "Nuketown_Yellow_House", "", "")
Attic = Room("Yellow House Attic", "", None, "Yellow_House_Kitchen", "", "")
Watermelon_Attic = Room("Attic", "", None, "Attic", "", "")
Attic_Stairs = Room("Attic Stairs", "", None, "Attic", "", "`")
East_Side_attic = Room("East-Side Attic", "", None, "Attic_Stairs", "", "")
Rest_Room = Room("Rest Room", "", None, "East-Side Attic", "", "")
Attic_Hallway = Room("Hallway", "", None, "", "", "")
GBO_Game_Room = Room("G-BO Game-Room", "", None, "", "", "")
West_Side_Attic = Room("West-Side Attic", "", None, "", "", "")
Quad_Studios = Room("Quad Studios", "", None, "", "", "")
hp_Afro_Repair = Room("hp Afro Repair", "", None, "", "", "")
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
