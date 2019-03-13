world_map = {
    'Place Unknown Nuketown': {
        'NAME': "Nuketown Blue House",
        'DESCRIPTION': "This is an abandon house but people come here to relax."
        "There are is an letter on the floor at the door.",
        'PATHS': {
            'WEST': "Looped_Road"
        },
        'LOOPED_ROAD': {
            'NAME': "West_side of The Looped_Road",
            'DESCRIPTION': "There is a blue car on your right and i suggest you not to the car.",
            'PATHS': {
                'EAST': "Nuketown Yellow House"
            },
            'Place_Unknown_Nuketown': {
                'NAME': "Nuketown Yellow House",
                'DESCRIPTION': "There's is a statue in the house as the door is wide open0",
                'PATHS': {
                    'EAST': "Yellow House Kitchen"
                },
                'Nuketown Yellow House': {
                    'NAME': "Yellow House Kitchen",
                    'DESCRIPTION': "There's a class cup on the counter and a sword"
                    "The sword is glowing red and a lantern is on the floor.There's stairs going south",
                    'PATHS': {
                        'SOUTH': "Attic"
                    },
                    'Attic': {
                        'NAME': "Yellow House Attic",
                        'DESCRIPTION': "It's dark in here you should use the lantern",
                        'PATHS': {
                            'SOUTH': "Attic"
                        },
                        'Attic': {
                            'NAME': "Attic",
                            'DESCRIPTION': "This is an huge attic."
                                           "Watch your step going down the stairs in here.",
                            'PATHS': {
                                'WEST': "Attic"
                            },
                            'Attic': {
                                'NAME': "Attic Stairs",
                                'DESCRIPTION': "You stepped on an broke step and fell through the steps "
                                               "There's Keys on the floor"
                                               "An thief is on the floor kill him before you get robbed.",
                                'PATHS': {
                                    'EAST': "East-side Attic"
                                },
                                'Attic': {
                                    'NAME': "East-Side Attic",
                                    'DESCRIPTION': "There's an sword glowing blue and a door",
                                    'PATHS': {
                                        'EAST': "Place Unknown Nuketown"
                                    },
                                    'Place Unknown Nuketown': {
                                        'NAME': "Rest Room",
                                        'DESCRIPTION': "There's and backpack on the floor"
                                                       "Food and water on the back pack ",
                                        'PATHS': {
                                            'NORTH': "Place Unknown Nuketown"
                                        },
                                        'Place Unknown Nuketown': {
                                            'NAME': "Attic Hallway",
                                            'DESCRIPTION': "There's an room ahead with the same"
                                                           "statue from the Yellow House",
                                            'PATHS': {
                                                'WEST': "Place Unknown Nuketown"
                                            },
                                            'PLace Unknown Nuketown': {
                                                'NAME': "G-BO Game-Room",
                                                'DESCRIPTION': "There's an rubber ducky on the floor and a phone",
                                                'PATHS': {
                                                    'WEST': "Place Unknown Nuketown"
                                                },
                                                'Place Unknown Nuketown': {
                                                    'NAME': "West-Side Attic",
                                                    'DESCRIPTION': "An witches broom is on the wall."
                                                                   "There's and door ahead with lock on it",
                                                    'PATHS': {
                                                       'WEST': "Quad Studios"
                                                    },
                                                    'Place Unknown Nuketown': {
                                                        'NAME': "Quad Studios",
                                                        'DESCRIPTION': "The Roof comes off soon as you come in"
                                                                       "An orc is on the wall look at you"
                                                                       "you should protect yourself before you die",
                                                        'PATHS': {
                                                            "North": "Place Unknown Nuketown"
                                                        },
                                                        'Place Unknown Nuketown': {
                                                            'NAME': "hp Afro Repairs",
                                                            'DESCRIPTION': "Clouds sudden come out and you get iht "
                                                                           "with Lightning you fall on an bed with"
                                                                           "two other beds a bear is on an bed"
                                                                           "you should talk to him"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


playing = True
current_node = world_map["Place Unknown Nuketown"]
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

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
