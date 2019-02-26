world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now"
                    "now.There are two doors on the north wall",
        'PATHS': {
                'NORTH': "PARKING_LOT"
        },
        'PARKING_LOT': {
            'NAME': "The North Parking Lot",
            'DESCRIPTION': "There are a couple parked here",
            'PATHS': {
                'SOUTH': "R19A"
            }
        }
    }
}

# Controller
playing = True
current_node = world_map["R19A"]
directions = ['NORTH', 'SOUTH', 'EATS', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not found")


class Room(object):
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east


class Player(object):
    def __init__(self, starting_location,race):
        self.current_location = starting_location
        self.inventory = []
        self.race = race

    def move(self,new_location):
        """This moves the player to a new room.

        :param new_location: The room object of which are
        """
        self.current_location = new_location

    def find_next_room(direction):
        """This method searches the current room so see if a room

        :param direction:
        :return:
        """
        name _of_ room = getattr(self.current_location, directions)




R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A.north = parking_lot

R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None,)

player = Player (R19A)


playing = True
directions = ('north', 'south', 'east', 'west', 'up', 'down')

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
        print("Command Not found")

