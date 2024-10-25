def start_adventure():      # Getting ingredients to make a cake at Walmart
   print("You need to make a cake for your mom, but you don't have any of the ingredients. So you stand outside of a Walmart. Do you:")
   print("1. Enter the Walmart")
   print("2. Go back home")

   choice = input("> ")

   if choice == "1":
       enter_walmart()
   
   elif choice == "2":
       go_home()
      

   else:
       print("Invalid choice. Try again.")
       start_adventure()


def enter_walmart():
   print("You start the adventure by walking into the store where should you start...")

def go_home():
    print("You decide to go back home, your mother is upset that there is no cake and kicks you out of the house.")     # first ending
    exit()
  

start_adventure()

def first_stop():
   print("You need to start collecting your ingredients. Do you:")
   print("1. Start in the candy aisle")
   print("2. Start in the baking aisle")
   print("3. Start in furniture aisle")

   choice = input("> ")
   if choice == "1":
       enter_candy()


   elif choice == "2":
       enter_baking()


   elif choice == "3":
       enter_furniture()
 
   else:
       print("Invalid choice. Try again.")
       first_stop()

def enter_candy():
   print("You decide that the cake can wait, you're starving!")
   print("Because you bought candy,you end up getting diabetes, causing you many health problems.")       #2nd ending??
   exit()


def enter_baking():
   print("You successfully make it to the aisle and are able to find the flour, but you're missing something...")


def enter_furniture():
   print("You went to the wrong aisle, and end up wasting too much time looking at furniture, you barely have enough time to collect flour...")

first_stop()

def second_stop():
   print("But you realize you can't find the baking soda. Do you:")
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
   print("You ask an employee, befriend them, and you together find the baking soda.")


def keep_looking():
   print("After looking for a few more minutes you finally find the baking soda.")


def give_up():
   print("You give up and just go home, your mother is very disappointed")      # 3rd ending
   exit()

second_stop()

def third_stop():
   print("You need to continue collecting ingredients, but you hear a strange sound. Do you:")
   print("1. Go a different direction")
   print("2. Continue anyway")

   choice = input("> ")

   if choice == "1":
       leave()

   elif choice == "2":
       unexpented_attack()

   else:
       print("Try again.")
       third_stop()

def leave():
   print("You decide to go a different direction, and are able to easily located the next to ingredients, salt and sugar.")


def unexpented_attack():           
   print("You continue towards the noise and come across a wild Karen.")
   karen_attack()


def karen_attack():
   print("She sees you and attacks; her verbal assault causes you to die of embarrassment.")    # 4th ending??
   exit()

third_stop()

def forth_stop():
   print("You have 2 ingredients left to collect. Where should you go next:")
   print("1. The office and art department")
   print("2. The dairy section")
   print("3. The electronics department")

   choice = input("> ")

   if choice == "1":
       enter_office()
   
   elif choice == "2":
       enter_dairy()

   elif choice == "3":
       enter_electronics()
   else:
       print("Invalid choice. Try again.")
       forth_stop()

def enter_office():
    print("You honeslty don't know way you came this way, you turn back and go to the dairy department.")
    enter_dairy()

def enter_dairy():
    print("You make it to the dairy section, and are able to locate the butter, but something doesn't seem right... ")

def enter_electronics():
    print("You go to the electronics and think that maybe your mother would like something other than a cake...")
    print("You decide your mom doesn't need cake, what she really needs is a new TV")               # 5th ending?
    exit()

forth_stop()


def fifth_stop():
    print("You feel like something or someone is watching you...")
    print("1. Look for this creature")
    print("2. Ignore it ")
    print("3. Start running")

    choice = input("> ")

    if choice == "1":
        enter_creature()

    elif choice == "2":
        enter_ignore()

    elif choice == "3":
        enter_running()

    else:
        print("Invalid choice. Try again.")
        fifth_stop()

def enter_creature():
    print("")

def enter_ignore():
    print("")

def enter_running():
    print("")

fifth_stop()