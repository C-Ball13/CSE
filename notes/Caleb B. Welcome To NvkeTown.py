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
                        'DESCRIPTION': "It's dark in here you should use the lantern if you picked it up",
                        'PATHS': {
                            'SOUTH': "Attic"
                        },
                        'Attic': {
                            'NAME': "Attic",
                            'DESCRIPTION': "This is an huge attic "
                        }
                    }
                }
            }
        }
    }
}
