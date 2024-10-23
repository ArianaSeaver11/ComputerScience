def start_adventure():      # Getting ingredients to make a cake at Walmart 
    print("You stand outside the entrance of a Walmart. Do you:")
    print("1. Enter the Walmart")
    print("2. Go back home")

    choice = input("> ")

    if choice == "1":
        enter_walmart()
    elif choice =="2":
        go_home()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

def enter_walmart():
    print("You start the adventure by walking into the store when you see your first problem...")

def go_home():
    print("You decide that it's not worth going shopping today and head home, causing you to starve to death.") #First ending


start_adventure()

def first_stop():
    print("You need to start collecting your ingredients. Do you:")
    print("1. Start in the candy aisle")
    print("2. Start in the baking aisle")
    print("3. Start in furniture aisle")

    choice = input("> ")
    if choice == "2":
        enter_baking()
   
    else:
        print("Try again, you when to the wrong aisle")
        first_stop()


def enter_candy():
    print("")

def enter_baking():
    print("You successfully make it to the correct and find the flour, but you're missing something...")

first_stop()

def second_stop():
    print("You can't find the baking soda. Do you:")
    print("1. Ask for help")
    print("2. Keep looking ")
    print("3. Give up")

    choice = input("> ")

    if choice == "1":
        ask_help()
    elif choice == "2":
        keep_looking()
    elif choice == "3":
        give_up()
    else:
        print("Try again.")
        second_stop()

def ask_help():
    print("you befriend an employee, and you together find it.")

def keep_looking():
    print("After looking for a few more minutes you find it.")

def give_up():
    print("You don't get the need ingredients and...")      # 2nd ending??

second_stop()

def third_stop():
    print("you need to continue collecting ingredients, but you heard a strange sound. Do you:")
    print("1. you decide to go a different dircetion")
    print("2. you decide to continue anyway")

    choice = input("> ")

    if choice == "1":
        leave()

    elif choice == "2":
        unexpented_attack()

    else:
        print("Try again.")
        third_stop()

def leave():
    print("")

def unexpented_attack():            # maybe third ending??
    print("")

third_stop()

def forth_stop():
    print("you still have ingredients to collect. Where should you go next:")
    print("1. go to the spices aisle")
    print("2. go to the flavoring aisle")
    print("3.")