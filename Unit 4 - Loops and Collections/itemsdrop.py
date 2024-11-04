import random
def drop_item():
    roll = random.randint(0,10000)
    if roll < 7000:
        print("Normal item")

    elif roll < 9000:
        print("Magic item")
    elif roll < 9900:
        print("Rare itme")

    elif roll < 9990:
        print("Legndary item")

    elif roll <= 10000:
        print("Uber item")

    if input("Another drop?\n") == "y":
        drop_item()

drop_item()
