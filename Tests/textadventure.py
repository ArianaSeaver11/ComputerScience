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

def first_aisle():
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
       first_aisle()

def enter_candy():
   print("You decide that the cake can wait, you're starving!")
   print("Because you bought candy,you end up getting diabetes, causing you many health problems.")       #2nd ending??
   exit()


def enter_baking():
   print("You successfully make it to the aisle and are able to find the flour, but you're missing something...")


def enter_furniture():
   print("You went to the wrong aisle, and end up wasting too much time looking at furniture, you barely have enough time to collect flour...")

first_aisle()

def finding_baking_soda():
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
       finding_baking_soda()


def ask_help():
   print("You ask an employee, befriend them, and you together find the baking soda.")


def keep_looking():
   print("After looking for a few more minutes you finally find the baking soda.")


def give_up():
   print("You give up and just go home, your mother is very disappointed")      # 3rd ending
   exit()

finding_baking_soda()

def strange_sound():
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
       strange_sound()

def leave():
   print("You decide to go a different direction, and are able to easily located the next two ingredients, salt and sugar.")


def unexpented_attack():           
   print("You continue towards the noise and come across a wild Karen.")
   karen_attack()


def karen_attack():
   print("She sees you and attacks; her verbal assault causes you to die of embarrassment.")    # 4th ending??
   exit()

strange_sound()

def finding_the_butter():
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
       finding_the_butter()

def enter_office():
    print("You honeslty don't know way you came this way, you turn back and go to the dairy department.")
    enter_dairy()

def enter_dairy():
    print("You make it to the dairy section, and are able to locate the butter, but something doesn't seem right... ")

def enter_electronics():
    print("You go to the electronics and think that maybe your mother would like something other than a cake...")
    print("You decide your mom doesn't need cake, what she really needs is a new TV")               # 5th ending?
    exit()

finding_the_butter()


def weird_creature():
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
        weird_creature()

def enter_creature():
    print("You look up and see that sitting on top of shelf is The Gale Luis.")
    print("You try not to disturb her, and keep walking.")


def enter_ignore():
    print("You decide that this creature probably wont hurt you and carry on.")

def enter_running():
    print("You run for a couple of minutes, you stop when you no longer feel their eyes, but it seems that your lost...")
    enter_starvation()

def enter_starvation():
    print("You are unable to find your way back or out of the store, and end up dying of starvation.")
    exit()

weird_creature()

def poultry_section():
    print("The only thing left to find is the eggs. Do you:")
    print("1. Start on the left side of aisle.")
    print("2. Start on the right side of the aisle.")

    choice = input("> ")

    if choice == "1":
        enter_left_side()

    elif choice == "2":
        enter_right_side()

    else:
        print("Invalid choice. Try again")
        poultry_section()

def enter_left_side():
    print("You look you everywhere on the left, but can't find it, so you moce to the right side.")
    enter_right_side()

def enter_right_side():
    print("You are able to quickly find the eggs and head to the check out.")

poultry_section()

def check_out():
    print("You finally have the items collected. Do you:")
    print("1. Self checkout ")
    print("2. Get in the other checkout lanes.")

    choice = input("> ")

    if choice == "1":
        enter_self_chechkout()

    elif choice == "2":
        enter_checkout_line()

    else:
        print("Invalid choice. Try again")

def  enter_self_chechkout():
    print("You are able to pay for everything and are able to leave the store.")
    print("You are able to make your mom a cake, so you lets you to continue to live in her basement.")
    enter_the_end()

def enter_checkout_line():
    print("You have to wait in a long line, and are finally able to leave.")
    print("You bake your mom a cake and she excepts your offering, and no longer wants to kick you out of the house.")
    enter_the_end()

def enter_the_end():
    print("You finished!! You successfully completed the task.")
    print("THE END")

check_out()
