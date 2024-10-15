# Expection Handling 
# Write a program that asks for 2 numbers and divides them

# if    =   try 
# elif = except with error type
# else  =   except 
def divide_two_numbers():
    try:     # we always enter the try block, there is no condition 
        x = int(input("What is the first number?\n>"))
        y = int(input("What is the second number?\n>"))
        print(x / y)

    except ZeroDivisionError:
        print("Cannot divide by zer, try again.")

    except ValueError:
        print("Please enter a vaild numerical symbol, try again")
        divide_two_numbers()

    except:     # If anything in the try block creates an error, 
            # the try block stops immediately and the except is ran instead
            # the rest of the try blokc never finishes running, its skipped
            # If the try blokc excutes without error, the except is skipped
            # The only way to get into the except is to "throw" an error
        print("Get help")
        divide_two_numbers()    # tell the function to run again

divide_two_numbers()

