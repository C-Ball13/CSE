world_map= {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the clasroom you are in right now",
    "Now.There are two doors on the north wall"
        'PATHS': {
            'North': "PARKING_LOT"
        },
        'PARKING_LOT': {
            'NAME': "The North Parking Lot",
            'DESCRIPTION': "There are a couple parked here",
            'PATHS': {
                'South': "R19A"
             }
        }
    }
}

# Controller
playing = True
current_node = world_map["R19A"]
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lover() in['q','quit','exit']: