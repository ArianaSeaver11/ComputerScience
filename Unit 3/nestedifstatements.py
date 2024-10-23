# Nested if statements 

prime = True 
cost = 20 
age = 17
consent = False

if prime:
    if age >= 18:
        print("Free Shipping Ig")
    elif consent:
        print("free shipping ")
    else: 
        print("u fake tho")

elif cost >= 25:
    if age >= 18:
        print("Free Shipping Ig")
    elif consent:
        print("free shipping ")
    else: 
        print("u fake tho")

else:
    print("Nope, no shipping")


# Decide if we need an umbrella
# You need an umbrella if its raining AND you are going outside that day.

raining = input("Is it raining outside?\n>")

if raining.lower() == "yes":
    outside = input("Do you planning on going outside?\n>")
   
    if outside.lower() == "yes":
        print("Bring umbrella")
    else: 
        print("No umbrella")
else: 
    print("no umbrella")


