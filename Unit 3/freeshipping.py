# Create a function calle dfree_shipping
# That tells you if you qualify for free shipping or not
# You only get free shipping if
# You are a Prime member OR order is at least $25 
# You are at least 18 years old OR have parent consent
# Your function should take four parameters 
# prime (boolean), cost (float), age (int), consent (bool)
# HINT: 
# You can use more than one logical operator is a condtion
# Use paraenthesis to group if needed 


def free_shipping(member, price, age, consent):
    if member == True or price >= 25:
        print("free shipping")
    else:
        print("no free shipping")

    if age <= 18 or consent == True:
        print("free shipping")

    else:
        print("nope, no free shipping")

free_shipping(True, 30, 89, True)