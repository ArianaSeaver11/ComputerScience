# String functions 
# String functions are a group of functions that modify strings
# .lower()
# .lower() changes the string to be all lowercase
# Can go after any kind of string
# .upper() changes the string to uppercase
# .captialize() changes the entire string to lowercase, then capilizes the first letter
# "Hello World!" > "Hello world!"

# .title() changes the entire string to titlecase (first letter in every word)
# "hello world" > "Hello World"

#.swpcase() inverts the capitalization of each character
# "Hello World!" > "hELLO wORLD!"




x = "Pigs"
x =x.lower()
print(x)


score = 0
one = input("What is a number greater than 4 and less than 6?\n>")
if one == "5":
    score = score + 1
    print("Correct")

two = input("a number equal to 35?\n>")
if two == "35":
    score = score + 1
    print("Correct")

three = input("How old is santa?\n>")
if three == "old":
    score = score + 1
    print("Correct")

four = input("Best color?\n>")
if four == "green":
    score = score + 1
    print("Correct")

five = input("What's the color of the sky?\n>")
if five == "blue":
    score = score + 1
    print("Correct")

print(score)

def tall_score():
    score = 0
    if one == "5":
        score = score + 1
        print("Correct")
    
    if two == "35":
        score = score + 1
        print("Correct")

print(str(score) + "/5")




