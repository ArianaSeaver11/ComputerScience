# If statements evaluate boolean expressions!
# They make decisions about which code to run next

# Take a temperature
# Print "<temperature> is hot" if its >= 80
# Otherwise, print "<temperature> is not hot"
temp = input("What's the temperature in F?\n>")
temp = int(temp)

# if <boolean expression>:
# This should remind you of wrinting a function
# def <name>(): 
if temp >= 80:
    print(str(temp) + " degrees is hot!")

if temp < 80:
    print(str(temp) + " degrees is not hot...")     #Or "else" statement

else:       #Otherwise....
    print(str(temp) + " degrees is not hot...")

# Not all if statements need an else, in fact NONE of them NEED an else
# Else statements are an option, they are optional
# All else statements must have a corresponding if statement
# Else statements cannont exist alone
# An if staement can only have ONE else

# Create a program that asks for a password
# If the password is correct, print ACCESS GRANTED 
# Otherwise, print ACCESS DENIED
# The password is skibidi68.9
real_pass = "skibidi68"
input_pass = input("Whats the password\n>")

if real_pass == real_pass:
    print("ACCESS GRANTED")

else:
    print("ACCESS DENIED")


# Activity 2, electric boogaloo
#Create a five question quiz that prints your score at the end 
#Choose any five questions
#EZ

q_one = "5"
q_one = input("What is 3 + 2?\n>")
if q_one == q_one:
    print("Correct")