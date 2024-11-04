import random
# Python has 4 types of collections
# Tuple
#Set
# >List
# >Dictionary

# Today, were going to focus on lists
# A list is a way to store more than 1 value in a single varible 
# The values in the list are called ITEMS
# Items can be acces by their INDEX (postion in the list) indices
# IDEX                          0                      1        2                   3               4                       
best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]
best_years = [1776, 1985, 1994, 1957, 2016]
myint = 3

print(len(best_elden_ring_weapons))


print(best_years[0])
print(best_elden_ring_weapons[0])                                # print the first item
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])   # print the last item

#List items can be changed!!
best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

# List functions!
# .pop()
# Removes an item at a given postion
best_elden_ring_weapons.pop(1)      # Remove Moonveil from the game

# .remove()
# Removes an item by value- removes the first instance of the value
best_elden_ring_weapons.remove("Blasphemous Blade")        # If the value doesn't exist, it error:(

# .append()
# Adds the value as a new item to the end of the list
best_elden_ring_weapons.append("Death's Poker")

numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100) ]
print(numbers)

#.sort()
# Sorts the numbers from smallest to greatest
numbers.sort()
print(numbers)

#max()
# Prints the largest number in the list!
print(max(numbers))

#min()
# Prints the smallest number in the lsut!
print(min(numbers))

#Strings.... are just ... lists of charaxters :O
print(len("Osowski"))
print("your mom"[4])



