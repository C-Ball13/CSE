world_map = {}


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.character = []


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """this move the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, directions):
        """This method searches the current room so see if a room
               exists in that direction.

        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
    name_of_room = getattr(self.current_location, directions)
    return \globals()[name_of_room]



Place_Unknown_Nuketown = Room("Nuketown Blue House", "This is where you are now", 'Looped_Road')
Looped_Road = Room("WestSide of looped Road", "", None, "Place Unknown Nuketown")

player = Player(Place_Unknown_Nuketown)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

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