world_map = {
class Room(object):
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east


Place_Unknown_Nuketown = Room("Blue House")
Looped_road = Room("Looped_Road ")
}