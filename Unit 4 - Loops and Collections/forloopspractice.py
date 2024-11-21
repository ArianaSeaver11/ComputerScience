# For loops review
# for loops allow us to iterate through a list!
#Iterate: perform repeatedly
# To do something repeatedly
# to look at every item in a list, one by one

# Basic Syntax
# Syntax: The "grammar" of the code

pokemon_cards = ["Squirtle", "Bidoof", "Zigzagoon", "Charizard"]

for card in pokemon_cards:
    print("The next car is..")
    print(card)

route = ["Home", "Tace Bell", "The Park", "Goodwill", "Home"]
#Changing your mind can soemthimes be the most difficult thing you ever do
# You need to look at mutiple list items during the one iteration
# Doing "For item in list", doesn't really work...
# For item in list only allow you to access one list item per iteration 
for location in route:
    print("You are traveling from " + location + " to " + location[1])
    # This doesn't work!!!!

# If you need to access multiple list items during the same iteration,
# Using "For variable in range()"" is preferred
for i in range(0, len(route)):  # Creates a list [0, 1, 2, 3, 4]
   # Use a try/except to block index out of range error
   #Error will happen on the last iteration
   # Because i+1 would be larger than there are items in the list
    try:
        print("You are traveling from" + route[i] + " to " + route[i+1])
    except:
        print("Route finished!")