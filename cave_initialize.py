
# =====================
# cave_initialize.py
# =====================

# For cave_initialize we create a shelve for locations and vocabulary
# This is the initialization setup to convert locations and vocabulary from dictionary to shelve
# NOTE: shelve keys have to be strings. That is why we convert the numeric values e.g. from 0 to string '0'
# NOTE: After creating this cave_initialize file, you have to run it so it creates shelves "location" and "vocabularies"

import shelve

locations = shelve.open("locations")

locations['0'] = {"desc": "This is the exit",
                  "exits": {},
                  "namedExits": {}}

locations['1'] = {"desc": "This is the Road",
                  "exits": {"W": '2', "E": '3', "N": '5', "S": '4', "Q": '0'},  # We also convert numerics her to strings
                  "namedExits": {"2": '2', "3": '3', "5": '5', "4": '4'}}

locations['2'] = {"desc": "This is the Hill",
                  "exits": {"N": '5', "Q": '0'},
                  "namedExits": {"5": '5'}}

locations['3'] = {"desc": "This is the building",
                  "exits": {"W": '1', "Q": '0'},
                  "namedExits": {"1": '1'}}

locations['4'] = {"desc": "This is the Valley",
                  "exits": {"N": '1', "W": '2', "Q": '0'},
                  "namedExits": {"1": '1', "2": '2'}}

locations['5'] = {"desc": "This is the Forest",
                  "exits": {"W": '2', "S": '1', "Q": '0'},
                  "namedExits": {"2": '2', "1": '1'}}

locations.close()

vocabulary = shelve.open("vocabulary")
vocabulary["QUIT"] = "Q"
vocabulary["NORTH"] = "N"
vocabulary["SOUTH"] = "S"
vocabulary["EAST"] = "E"
vocabulary["WEST"] = "W"
vocabulary["ROAD"] = "1"
vocabulary["HILL"] = "2"
vocabulary["BUILDING"] = "3"
vocabulary["VALLEY"] = "4"
vocabulary["FOREST"] = "5"

vocabulary.close()


