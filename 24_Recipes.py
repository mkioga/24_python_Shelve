
# ===============
# 24_Recipes.py
# ===============

# =============================================
# Updating values stored in a shelve
# =============================================

# NOTE: we are using new python file called 24_Recipes (still under 24_Shelve project)

# we will look at the ways to update values stored in a shelve
# we will also look at a common way to increase performance
# And also go through a problem that baffles people new to the shelve module

# first we import shelve

import shelve

# Then we create "list" with recipes

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# Now we save above lists to a shelve called "recipes"
# Note that we have not stored "soup" in the shelve
# When you ran this code, a database called recipes.dat is created to the left

with shelve.open("recipes") as recipes:  # save to shelve named recipes
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast # Add each list above to shelve[key] with same name
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["pasta"] = pasta

# Since the recipes data (excluding soup) has been written to the recipes shelve database,
# we can comment out the code above because the same things don't need to be added to the database over and over again

# We now print the existing "recipes". Result should only have "blt", beans_on_toast, scrambled_eggs and pasta

    for snack in recipes:
        print(snack, recipes[snack])   # This gives the four recipes added to shelve "recipes" (before code below is ran)

    recipes["soup"] = soup  # Now we add "soup" to recipe
    print()
    for snack2 in recipes:
        print(snack2, recipes[snack2])  # result now shows all 5 recipes including "soup"

print()
print("="*40)

# ================================================
# "appending" items to a list in shelve
# ================================================

# Now we want to add "butter" to "blt" and "tomato" to "pasta"



blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# first we ran this command to create database for recipes2, then comment out the code after recipes2.dat is created
# to avoid overwriting every time code is run

with shelve.open("recipes2") as recipes2:  # save to shelve named recipes2
    # recipes2["blt"] = blt
    # recipes2["beans_on_toast"] = beans_on_toast # Add each list above to shelve[key] with same name
    # recipes2["scrambled_eggs"] = scrambled_eggs
    # recipes2["pasta"] = pasta
    # recipes2["soup"] = soup

    # Now we "append" butter to blt and tomato to pasta

    recipes2["blt"].append("butter")
    recipes2["pasta"].append("tomato")

    # When we initially ran the code after the updates above, we see butter and tomato are not added

    for snack in recipes2:
        print(snack, recipes2[snack])   # This gives the four recipes added to shelve "recipes" (before code below is ran)

    # The reason it was not updated is because the shelve has no way to know that these lists have changed
    # What happened is we appended to a copy of lists that are in memory but we have not provided the trigger for the
    # shelve to write the data back to it again
    # The reason for this is to keep disk access to a minimum so that values aren't continually reintroduced
    # But the side effect is when accessing the same key values, it reads the original values from the shelve


print("="*40)


# There are two ways to resolve the above issue of updating lists in shelve

# Method 1
# We can assign the list we want to update to a new variable
# then append new items to that new variable
# Then assign the original list the contents of that new updated variable

# Advantages of this method is that you are working with objects in memory with all the
# performance benefits that provides because it is faster than continually reading and writing to disk

# Disadvantages is you need to make sure you reassign any immutable objects that have changed back
# to their keys in the shelve


blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]


with shelve.open("recipes3") as recipes3:  # save to shelve named recipes3
    recipes3["blt"] = blt
    recipes3["beans_on_toast"] = beans_on_toast # Add each list above to shelve[key] with same name
    recipes3["scrambled_eggs"] = scrambled_eggs
    recipes3["pasta"] = pasta
    recipes3["soup"] = soup


    temp_list = recipes3["blt"]  # we assign current "blt" to temp_list
    print(temp_list)  # we see temp_list has original values of blt
    temp_list.append("butter")  # now we append butter to temp_list
    print(temp_list)  # We see temp_list is now updated
    recipes3["blt"] = temp_list  # Now we assign new temp_list to recipes["blt"]

    # we do same thing for pasta
    print()
    temp_list = recipes3["pasta"]
    print(temp_list)
    temp_list.append("tomato")
    print(temp_list)
    recipes3["pasta"] = temp_list

    # When we iterate through all the items, we now see blt and pasta are updated
    print()
    for snack in recipes3:
        print(snack, recipes3[snack])


print("="*40)



# Method 2

# =========================
# using "writeback=True"
# =========================

# When we use "writeback" python keeps the item in memory cache and does not update the shelve files until
# you close the shelve or use the "sync" method
# If there have been a lot of changes, closing the shelf can take a while because they all have to be
# written to disk at once.

# Advantage is we have simpler code
# Disadvantage is there is higher memory usage depending on the amount of data you're working with.

# There is a potential problem that can arise when using the "sync" method
# Sync causes all entries in the cache to be written to disk, but it also clears the cache as well.
# Sync is called automatically when the shelve is closed, but you can also use it any
# time you want data files to be updated

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]


with shelve.open("recipes4", writeback=True) as recipes4:  # use writeback=True to write back to database
    recipes4["blt"] = blt
    recipes4["beans_on_toast"] = beans_on_toast
    recipes4["scrambled_eggs"] = scrambled_eggs
    recipes4["pasta"] = pasta
    recipes4["soup"] = soup

    recipes4["soup"].append("croutons")  # We append croutons to soup. NOTE: append only takes one argument

    # We see soup is updated

    print()
    for snack in recipes4:
        print(snack, recipes4[snack])

print("="*40)


# So far we have appended to our lists by retrieving them from the shelve by key
# And that is usually the best way to do things

# However in a situation where you want to update a list immediately after adding
# it to the shelve, you don't want to use sync because sync will clear cache after writing to disk

# So if you want to use sync method, do not update objects like in example below.


blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]


with shelve.open("recipes5", writeback=True) as recipes5:  # use writeback=True to write back to database
    recipes5["blt"] = blt
    recipes5["beans_on_toast"] = beans_on_toast
    recipes5["scrambled_eggs"] = scrambled_eggs
    recipes5["pasta"] = pasta
    recipes5["soup"] = soup

    recipes5.sync()  # sync writes to disk and clears cache

    # This append adds "cream" to soup in cache, but there is no corresponding object in the cache anymore
    # because of recipes5.sync() above which cleared the cache. hence soup will not be updated in disk
    # And the print function reads from disk.

    soup.append("cream")

    print()
    for snack in recipes5:
        print(snack, recipes5[snack])  # So print will only show origiinal results written to disk by sync before the update

print("="*40)


# Disadvantages of shelve module

# "shelve" module has some drawbacks and may not be suitable for some applications.

# Example 1
# because values are pickled before being stored, and unpickled when values are read back,
# if your values are really complex, this pickling and unpickling may impact significant overhead in performance
# and slow down your application.

# Different systems use different underlying technologies for storing shelve, so that data is not platform agnostic
# so if the application is likely to be moved to a new system, it must take its data with it, hence shelves
# probably are not the best solution because they may not work properly in that new environment.

# There is also a security threat if you use shelve files from untrusted sources e.g. from the internet.

# Therefore, although shelves can be used in appropriate places, it may be more suitable to store data in databases


# =============
# Errors
# =============

# Errors when converting a "dictionary" that is initialized using a literal, into a shelve
# Intellij syntax checking does not catch this error

# We are going to use this dictionary "books" and then later convert it to a shelve

books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled_eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]},
        "maintenance": {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}}


# So we are going to print elements from above dictionary to make sure it works
# The print works fine.

print(books["recipes"]["soup"])                # to print soup
print(books["recipes"]["scrambled_eggs"])
print(books["maintenance"]["loose"])

print("="*40)

# Now we want to convert above dictionary into a shelve

import shelve
books = shelve.open("book")  # we open with shelve
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_on_toast": ["beans", "bread"],
                     "scrambled_eggs": ["eggs", "butter", "milk"],
                     "soup": ["tin of soup"],
                     "pasta": ["pasta", "cheese"]}  # this comma after ]}, causing error. Remove it and it works

books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}


# we see that intellij does not catch any error.
# but when we run it, we get error "tuple indices must be integers or slices, not str"
# this is caused by above comma

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled_eggs"])
print(books["maintenance"]["loose"])
books.close()  # Then we need to close because we are not using "with"

print("="*40)

# so when converting from "dictionaries" to "shelve", make sure to watch for extra commas and brackets that may cause errors


# "shelve" challenge

# Switching dictionary to shelve and vice versa
# Modify this dictionary from past lesson to use shelves instead of dictionaries
# Do this by creating two programs.

# cave_initialize.py should create the two shelves.
# (location and vocabulary) with the appropriate keys and values.

# cave_game.py will then use the two shelves instead of dictionaries.
# Apart from opening and closing the shelves, cave_game will need only two
# changes to the actual code - remember that shelve keys must be strings.

# Just to be clear, cave_game.py will contain the code starting with "loc = 1"
# Everything before that (modified to use shelves) will be in cave_initialize.py



locations = {0: {"desc": "This is the exit",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "This is the Road",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "This is the Hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "This is the building",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "This is the Valley",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "This is the Forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",   # We update this dictionary with this
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}


# in below code under line with break
# We will test if the user is not quiting (loc is not equal to 0)
# Then create a combined directory by taking a copy of an instance of the
# "exits" dictionary and updating it to include the appropriate "namedExits"

# Explain (1), here we use ", ".join(locations[loc]["exits"].keys())"
# to extract the exits value from the master dictionary "locations"
# So we use "locations[loc]" to go to location 1 (section for road)
# Then we go further to "join(locations[loc]["exits"]" to extract key  named "exits"
# Then use "join(locations[loc]["exits"].keys())" to extract the "values" of "exits" key


loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys()) # Explain(1) Extract exits value from locations
    print("availableExits = {}".format(availableExits))
    print("You are in position: {}".format(loc))  # print position number which is loc
    print("Desc of your location: {}".format(locations[loc]["desc"])) # Description of your location is pulled from "loc" then "desc" keys

    if loc == 0:    # if location is 0, break (because you want to quit)
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


print("="*40)
