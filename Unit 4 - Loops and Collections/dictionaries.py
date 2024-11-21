# dictionary is a type of collection like a list 
# A list is a collection of items in a sequence
# A Dictionary is different 
# Dictionariesd store data in key-value pairs
# You can retrevie data quickly by using a unique key
# Instead of retreiving it by index (postion)

# Exampke
# Lists use brackets [], dictionaries use braces {}

ariana = {
    "name": "Ariana", 
    "age": 16,
    "city": "St. Michael",
    "pets": "none",
    "height": 5.4
}
# Each key must be unique

# Retrieving values form a dictionary
print(ariana["name"]) # Prints the name 
print(ariana["age"]) # Prints the age 

# This will error if you give a key that doesn't exist!
# 
# print(ariana["your mom"])  # this error!

# .get allows you to retrieve a value without erroring 
# When the key doesn't exist
# The sescond parameter is what is given if the value is not found 

print(ariana.get("height"))
print(ariana.get("country", "Country not found "))

# You can add new values to an existing dictionary
ariana["country"] = "USA"

# You can modify existing values
ariana["age"] = 16

# You can remove existing values
ariana.pop("pets")

# Iterate through a dictionary using a for loop!
for key, value in ariana.items():
    print(key + " = " + str(value))

# Dictoinary Functions
print(ariana.keys())    # returnd all keys
print(ariana.values())  # returns all values
print(ariana.items())   # returns all key-value paris
print(ariana.clear())   # returns allm items from the dictionary 


