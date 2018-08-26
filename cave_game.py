
# ===============
# cave_game.py
# ===============

# Now we will do cave_game.py to run the program using values created by cave_initialize.py

# NOTE: This is the explanation from previous code

# in below code under line with break
# We will test if the user is not quiting (loc is not equal to 0)
# Then create a combined directory by taking a copy of an instance of the
# "exits" dictionary and updating it to include the appropriate "namedExits"

# Explain (1), here we use ", ".join(locations[loc]["exits"].keys())"
# to extract the exits value from the master dictionary "locations"
# So we use "locations[loc]" to go to location 1 (section for road)
# Then we go further to "join(locations[loc]["exits"]" to extract key  named "exits"
# Then use "join(locations[loc]["exits"].keys())" to extract the "values" of "exits" key


# We import shelve because we will be using shelves

import shelve

# We then open the shelves (locations & vocabulary) created by cave_initialize.py

locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")

loc = '1'  # This was initially an integer, but we convert it to a string (since shelve keys use strings)

print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys()) # Explain(1) Extract exits value from locations
    print("availableExits = {}".format(availableExits))
    print("You are in position: {}".format(loc))  # print position number which is loc
    print("Desc of your location: {}".format(locations[loc]["desc"])) # Description of your location is pulled from "loc" then "desc" keys

    if loc == '0':    # We also convert this test to string. from 0 to '0'
        break
    else:
        allExits = locations[loc]["exits"].copy() # pull exits from locations using key "loc" and "exits"
        print("allExits before update: {}".format(allExits)) # AllExits before being added with namedExits
        allExits.update(locations[loc]["namedExits"]) # combine "exits" and "namedExits"
        print("allExits after update: {}".format(allExits)) # allExits after update

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
    print()

    # This is the code we will add for this step
    # We parse the user input (stored in "direction", and check if it exists in "vocabulary"

    if len(direction) > 1: # if user entered more than one letter, check vocabulary dictionary
        words = direction.split()  # We take input in "direction", split it by space, then assign it to variable "words"
        print("split words are: {}".format(words)) # We print words here just to see what it has. Not necessary for the code
        for word in words: # loop through all the entries in "words"
            if word in vocabulary: # if any of entries in "words" match key in vocabulary
                direction = vocabulary[word] # retrieve the "value" corresponding to "key" in vocabulary and assign it to direction
                break # Then we break from the "if word in words"

    # Then we use the new "direction" here as normal. so if user typed "QUIT", above code assigns "Q" to direction
    # Then in below code, direction will be "Q" and it will run as normal

    if direction in allExits: # here we test for "allExits"
        loc = allExits[direction]  # new loc is given value in combined dictionary "allExits"
        print("New position = : {}: Description = : {}".format(loc, locations[loc]))
    else:
        print("You cannot go in that direction")


# Make sure to close the shelves (locations & vocabulary) since we are not using "with"

vocabulary.close()
locations.close()
