x = 5

def my_function():     #define the function with a nmae
    print("Hello World")
    print("catdog")

print("Osowski r00lz d00d")
my_function()

def good_movies(movie1, movie2, movie3, movie4, movie5):
    print("My top 5 movies")
    print("1. Antman")
    print("2. New Groove")
    print("3. cars")
    print("4. cars 2")
    print("5. cars 3")
    
good_movies()

def add(x, y): 
    print(x + y)

x = 5     #global varible 

def my_function():
    add(5, 10)
add (2, 2)
add(33, 33)
add("cat", "dog")

#local variable or global varible 
def add(x,y):
    return x + y
solution  = add(5,10)
print(solution)


def my_function(a, b):   #you can put almost anything after return
    return a + b


def goofy(x, y, z):
    str1 = x * 5
    str2 = y * 2
    str3 = z * 3
    return x + y + z

goof_var = goofy("Cat", "dog", "rat")
print(goof_var)