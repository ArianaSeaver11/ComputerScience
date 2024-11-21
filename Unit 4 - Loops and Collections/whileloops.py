# There are a couple of types loops in python
# The for loop lets you iterate through a list 
# Great for looping a set number of times
# BUT WHAT IF we need to loop an uncertain number of times???
# ex. Entering your passward
# You could get it right the first tim
# It could take you a million tries
# Or anyting in between 


real_pass = "ninjalowtaper"
entered_pass = ""
attempts = 0
while entered_pass != real_pass:        # It will loop as long as this is true
    #Ask for the password
    entered_pass = input("Please enter the password\n>")
    attempts = attempts + 1
    #Check if the password is correct
    if entered_pass == real_pass:
        print("Access Granted")
    else:
        
        print("Access denied")
        print("try again...lol")
        print(str(attempts) + "attempts")

print("Welcome")

# With while loops, you need to be careful for infinite loops
# When you put your computer into rest mode, it has nightmares about infinite loops /joke
# An infinite loop happens when you enter a loop that can never be escaped
# Like black holes
# Don't create a black hole 
# Let's create a black hole

# REal world example

user_input = ""

while user_input != "exit":
    user_input = input("enter something!")
    print("type 'exit' to quit")
    print("You typed:" + user_input)

print("All done!")
