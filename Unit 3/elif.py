# the if statement has two buddies
# the first little buddies is the else statement 

x = 10

if x > 0:   # Not every if needs an else
    print("x is a postive number")

# the second little buddy is the elif (else if)
elif x <0:
    print("x is a negative number")

else:   # Else always needs an if 
    print("x is zero")


light = input("what color is the light?\n>")

if light.lower() == "green":
    print("GO")

elif light.lower() == "green":
    print("Stop if safe")

elif light.lower () == "red":
    print("STOP")

else:
    print("Yield")

######################################
x = 10 
if x > 5:
    print("x is greater than 5")

elif x > 8:
    print("x is greater than 8")

