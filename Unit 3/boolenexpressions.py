# Boolean Expression
#Kinda like a matmatical formula 
#  14 + 10 = 24     Algebra uses arithmetic operators 
# + - * ** % //
# Can only evalute to True or False
# 5 > 10 = False    Boolean Algebra uses comparison operators
# > < >= <= !=

print(5 > 10)    # Algebra 
print( 14 + 10)  # Boolean Algebra

x = 5           # SET x equal to 5, tell it what to be 
print(x == 5)   # GET x equal 5, ask a question / == asks, "Are you equal?"

# This is the PERFECT test question 
# What is the difference between = and == ?

print(4>= 2)        # True
print(1993 == 1993) # True
print(-90 < -99)    # False
print(10 != 10)     # False, "NOT"

# Boolean expressions quiz!
answer_one = input("Give me an integer that is negative\n>")
answer_one = int(answer_one)
print(answer_one < 0)

answer_two = input("Write the number 5\n>")
answer_two = int(answer_two)
print(answer_two == 5)

print("Walrus" + "Walrus")  #WalrusWalrus
print("Walrus" == "Walrus") # True
