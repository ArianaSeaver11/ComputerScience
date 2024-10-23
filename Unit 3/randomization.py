import random

r = random.randrange(0, 10) 
# the first number is inclusive, the second is exclusive
# 0 <= result < 10
print(r)


print("You have a 25 percent chance to win!")
p = random.random()
# random.random generates a random float between 0 and 1 
if p <= 0.25:
    print("You win")

else: 
    print("You lose")

