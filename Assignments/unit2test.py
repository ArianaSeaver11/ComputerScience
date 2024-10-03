#Question 1
word_one = input("Type random word\n>")
word_two = input("Type a second random word\n>")
word_three = input("Type third random word\n>")

print( word_one + " " + word_two + " " + word_three)
#Question 2
def add_three (x, y, z,):
    print(x + y + z)
    x = int(x)
    y = int(y)
    z = int(z)

x = input("random number")
y = input("Another random numeber")
z = input("Third random number")
x = int(x)
y = int(y)
z = int(z)
add_three(x, y, z)

#Question 3
def data_three():
    word = input("random word")
    integer = input("random integer")
    float_one = input("random decimal")
    integer = int(integer)
    float_one = float(float_one)
    word = str(word)
    print(float_one + integer)