wind = input("What is the wind speed\n>")
wind = int(wind)

if wind < 96:
    print("Category 1")

elif wind < 111:
    print("Category 2")

elif wind < 130:
    print("Category 3")

elif wind < 157:
    print("Category 4")

elif wind >= 157:
    print("Category 5")

else:
    print("Probably not a tropical storm")

