
# =============
# 24_Shelve.py
# =============

# Although pickle module is great for serializing objects, it has a drawback
# in that the objects have to be loaded into memory. That is fine in many situations
# but if you are dealing with a really large single object, like a large dictionary,
# then loading it to memory may not be a realistic option

# The "shelve" module provides a shelf, like a dictionary that is stored in a file rather
# than in memory. Like a dictionary, the shelf holds key value pairs, and the values can
# be anything that can be pickled.

# Shelf keys must be strings whereas dictionary keys can be immutable objects like tuples
# All methods that can be used with dictionaries can also be used with shelf objects
# So shelves can be thought of as persistent dictionaries

# Because the values are pickled when saved, you should only use files from trusted sources
# Don't use shelf files from untrusted sources

# To start using shelf, you have to import shelve library

import shelve

with shelve.open("ShelfTest") as fruit:  # Shelf are read/write, so no need to specify mode.
    fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
    fruit["apple"] = "Apple is a red crunchy fruit"
    fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
    fruit["grape"] = "Grapes grow in bunches"
    fruit["lime"] = "Lime is a sour green citrus fruit"

    print(fruit["lemon"])  # Access the shelf using key
    print(fruit["grape"])

print(fruit)   # This prints a shelf

print("="*40)

# NOTE: If the python file is shelve.py, (same as imported module "shelve", you will get an error.
# In my case, python file is named 24_Shelve.py, hence no error
# you can rename a python file by Right clicking it > Refactor > Rename

# Notice the created database "ShelfTest.dat" on the left side. This is where shelf data is stored
# The shelf may be stored in several files.
# Once the shelf is open, we can use it like a dictionary, Can assign values to keys, access individual values
# using the keys



# ===============================================================================
# One difference between shelve and dictionary, is there is no shelve literal
# ==============================================================================

# Dictionaries are unordered and contain key value pairs.
# The values are not accessed by an index but by means of a key.

with shelve.open("ShelfTest") as fruit:  # Shelf are read/write, so no need to specify mode.
    fruit = {"orange": "Orange is a sweet citrus fruit",   # We use a dictionary to assign values to fruit
            "apple": "Apple is a red crunchy fruit",
            "lemon": "Lemon is a sour yellow citrus fruit",
            "grape": "Grapes grow in bunches",
            "lime": "Lime is a sour green citrus fruit"}

    print(fruit["lemon"])  # Access the shelf using key. Even if you don't indent these, they still work
    print(fruit["grape"])

print(fruit)  # This gives a dictionary

print("="*40)

# Above example shows that you cannot initialize a shelf using a literal as we could with a dictionary



# Note that when using the with statement, it automatically closes the file when the with block finishes
# =================================================================

with shelve.open("ShelfTest") as fruit:  # Shelf are read/write, so no need to specify mode.
    fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
    fruit["apple"] = "Apple is a red crunchy fruit"
    fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
    fruit["grape"] = "Grapes grow in bunches"
    fruit["lime"] = "Lime is a sour green citrus fruit"

    print(fruit["lemon"])  # Access the shelf using key
    print(fruit["grape"])

print(fruit)   # here we can see fruit is a shelf and not a dictionary like above code

print("="*40)


# =======================================================================
# If you are not using with, it is your responsibility to close the loop
# =======================================================================

fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"

print(fruit["lemon"])  # Access the shelf using key
print(fruit["grape"])
fruit.close()   # you will need to close fruit since you're not using with statement

print(fruit)   # here we can see fruit is a shelf and not a dictionary like above code

print("="*40)


# =================================================================
# You can store different data in shelve as shown below
# =================================================================

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"      # Can assign strings
    bike["engine_size"] = 250  # Can assign numbers

    print(bike["engine_size"])
    print(bike["color"])

print("="*40)


# Note that shelve is persistent to a file i.e. if you make an error, that error will still be in the database
# for example, we will run this oode first under "bike2". it will work and create a shelve file (bike2.dat)
# Now we make an error entering wrong engin_size spelling

with shelve.open("bike2") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"
    bike["engin_size"] = 250  # Make error and type engin_size (wrong spellin)

    print(bike["engine_size"])  # Then try to retrieve engine_size
    print(bike["engin_size"])   # This still pulls result because it is still in database
    print(bike["color"])

print("="*40)


# =================================================================
# Delete from shelve:
# =================================================================

# we know that there is an entry for engin_size in bike2.dat
# we can delete it using del command

with shelve.open("bike2") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"
    bike["engine_size"] = 250

    del bike["engin_size"]  # delete engin_size

    print(bike["engine_size"])
#    print(bike["engin_size"])   # This will give an error because "engin_size" no longer exist
    print(bike["color"])

print("="*40)

# =================================================================
# you can use for loop to iterate through the keys to pull values:
# =================================================================

with shelve.open("bike3") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"
    bike["engine_size"] = 250

    for key in bike:
        print("{} : {}".format(key, bike[key]))   # Can print key and value

print("="*40)



# ==============================
# Manipulating data with shelve:
# ==============================

# you can update values using shelf as shown below
# in this case, we have original "lime" and then updated its description and it was updated

fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"

print("First lime description")
print(fruit["lime"])  # print first lime description
print()

fruit["lime"] = "great with tequila"  # update description of lime
print("Second lime description")
print(fruit["lime"])   # print second lime description
print()

for snack in fruit:
    print(snack + ": " + fruit[snack]) # print all of them. key and value using for loop


fruit.close()   # you will need to close fruit since you're not using with statement

print(fruit)   # here we can see fruit is a shelf and not a dictionary like above code

print("="*40)


# ======================================================================
# Using "get" method in "shelve" to avoid error if wrong key is used:
# ======================================================================

# in a previous example, we saw if you try to print something and input a wrong key, you get an error
# we can use "get" method to avoid error if someone enters wrong key
# if user enters wrong key, it will give "None" and not an error


fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"


while True:
    shelf_key = input("Please enter a fruit: ")  # we enter a fruit to use as key
    if shelf_key == "quit":   # breaks loop if someone wants to quit
        break

    description = fruit.get(shelf_key)  # We get description using "get" method and passing it shelf_key we got from user
    print(description)  # Then we can print the description here

fruit.close()   # you will need to close fruit since you're not using with statement

print("="*40)


# If user input a key that is not in the keys, "get" prints "None"
# We can also specify default value for "get" to print if user input is not in keys


fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"


while True:
    shelf_key = input("Please enter a fruit: ")  # we enter a fruit to use as key
    if shelf_key == "quit":
        break

    description = fruit.get(shelf_key, "We don't have a " + shelf_key)  # Adds default output if key is not present
    print(description)

fruit.close()   # you will need to close fruit since you're not using with statement

print("="*40)



# Another way is to test if the input key is in the keys before printing
# ======================================================================

fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"

while True:
    shelf_key2 = input("Please enter a fruit: ")  # we enter a fruit to use as key
    if shelf_key2 == "quit":
        break

    if shelf_key2 in fruit:
        description = fruit[shelf_key2]  # We print description since we have tested and know it is there
        print(description)
    else:
        print("We don't have a " + shelf_key2)

fruit.close()   # you will need to close fruit since you're not using with statement

print("="*40)


# ======================================================================
# Sorting "keys" in "shelve"
# ======================================================================

# Remember that in "dictionaries", the keys are unsorted i.e. the order is undefined.
# Keys in "shelve" are also unsorted
# From results below, you see the results of the keys are unsorted.
# in some python implementations, they may be sorted because shelve is implemented from a database
# but we cannot trust that. But in this case, they are unsorted

fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"

for f in fruit:
    print(f + " - " + fruit[f])   # The results here are unsorted.

fruit.close()   # you will need to close fruit since you're not using with statement

print("="*40)



# We can make a sorted list as shown
# ======================================================================


fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"

ordered_keys = list(fruit.keys())  # we get the keys from fruit, put them in a list and assign them to ordered_keys
ordered_keys.sort()   # Now we sort the ordered_keys in the same variable (ordered_keys)

for f in ordered_keys:  # Now we iterate through the sorted keys
    print(f + " - " + fruit[f])   # And print the sorted keys. Should be in alphabetical order

fruit.close()   # you will need to close fruit since you're not using with statement

print("="*40)




# ======================================================================
# "values" and "items" methods in "shelve
# ======================================================================

# "values" and "items" methods behave the same in "shelve" as they do in "dictionaries"
# But the objects returned are not the same type.
# Their type depends on the implementation.

# in example below, we will use print "values" and "items" which is a sequence of tuples


fruit = shelve.open("ShelfTest")   # open shelve and assign it to fruit
fruit["orange"] = "Orange is a sweet citrus fruit"   # Save descriptions to fruit by key (orange in this case)
fruit["apple"] = "Apple is a red crunchy fruit"
fruit["lemon"] = "Lemon is a sour yellow citrus fruit"
fruit["grape"] = "Grapes grow in bunches"
fruit["lime"] = "Lime is a sour green citrus fruit"

for v in fruit.values():
    print(v)
print(fruit.values())

print()
for i in fruit.items():
    print(i)
print(fruit.items())

fruit.close()   # you will need to close fruit since you're not using with statement

print("="*40)

# instead of returning "dict_values" and "dict_items" objects,
# the "values" and "items" methods when called on a "shelve" return "ValuesView" and "ItemsView"
# These are "View" objects and hence cannot be modified

# Similarities between "Shelve" and "Dictionaries"

# Changes in the underlying shelve will be reflected in these view objects, just like dict_keys, dict_values or dict_items
# Code that works when using "dictionary" will always continue to work in "shelve" without modification
# The initialization will be different and the shelf has to be closed

# Differences between "shelve" and "dictionaries"

# "Shelve" key must be a "string", but "Dictionaries" can accept any immutable object as a key
