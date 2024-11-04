# For loops
# This is a big deal
# For loops allows the programer to REPEAT, or what we call LOOP

# Write a program that prints the numbers 1 through 10
# Each on a new line

fav_foods = ["Eggs Bennies", "Fried Chickie", "Mac n Cheese"]

#for <var> in <list>:

for i in range(90,101):
    print(i)

for food in fav_foods:
    print(food)
    #Runs all of the line inside the for loop
    # When it reaches the bottom of the list, it runs again
    # And moves on to the next item in the list
    # It ends when there are no list items left


for i in range(10,0,-1):    #START, STOP, STEP
    print(i)


# Sum of a list
nums = [97,41,6,878,19]
sum = 0
for n in nums:
    sum = sum + n

print(sum)

#Square of Each Number

ints = [3,2,5,4,1]
newlist = []

for i in ints:
    newlist.append(i*i)

print(newlist)


# Character Count
stringy = input("Please enter a string\n>")
numvowels = 0
for s in stringy:

    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1
print(numvowels)


# Print Multiplication Table
try:
    multi = int(input("Gimme an int yo!\n>"))
except: 
    print("womp womp")

for i in range(0,multi + 1):
    print(str(multi) + " x " + str(i) + " = " + str(multi*i))


#List of Names
names = ["Peter", "John", "Paul", "Luke"]
for name in names:
    print("Hello," + name + "!")

