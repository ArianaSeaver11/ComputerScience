import random
user_input = ""
number = random.randint(0,101)

while user_input != number:
    user_input = int(input("Type a number between 0 and 100\n>"))
    
    if number == user_input:
        print("Correct")

    elif user_input > number:
        print("Too high")

    elif user_input < number:
        print("Too low")
    
    else:
        print("Try again")

print("The number was..." + number)