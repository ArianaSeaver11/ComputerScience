# 2 basci fucntion
#You know soemthing is a function becasue is has () at the end 
#The stuff that goes in those ( are called parameters
#Pararmeters are the information the function needs to run
#I say junmp, you say how high? How high is the parameter
print("hello  world!") #Hello World is the parameter
input("What is your favorite animal\n>")
 #\n is called an escape character (linebreak)
      #input is never required, only use it when necessary

#varibles
# variable are a way to store data for later use in the program
#Syntax (grammer)
# <name> = <value> 
x = 5    # x is the variable name, 5 is the value
#snake name convention - all lowercase, underscored for spaces
# CONCISE: short and descriptive
username = "Seaver"     #Define string (string of characters)
fva_animal = "Cow"         #Define string 
total_poptarts = 12        #Define intereger (whole numbers)  #all good snakecase
percent_complete = 23.52    #define float (decimal numbers)
is_cool = True              #Define Boolean (true/False values)
first_letter = 'c'          #Define character( single keyboard symbol)

total_poptarts = 8      #Ressigning variable

# Arithmetic operators (sounds scary, just basic math)
#   +   -   *   /   **   %   //
print(2 + 2)            #>8
print("2" + "2")        #>22
print("cat" + "dog")        #catdog
print("cat" * 3)        #>catcatcat
print("cat" + 3)        #>ERROR: Cannot use + for string and int

my_variable = 2 + 3     #Arithmetic ooperation can be done anywhere

#Make some working programs
# 1. add two numbers using input
x = input("What is x?\n>")      #input function always returns a string
x = int(x)
y = input ("What is y?\n>") 
y = int(y)
print(x + y)

