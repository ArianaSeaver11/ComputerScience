from adafruit_circuitplayground import cp

# When the program finiches, the baord enters a "waiting" state
# -> flashes all green then off
# We do not want the program to ever end
# That's why we put our work in a while True
# -> runs forever

while True:
    x, y, z = cp.acceleration
    if x > 5:
        for i in range(1, 4):
            cp.pixels[i] = ((25, 0, 0))
        for i in range(6, 9): 
            cp.pixels[i] = ((0, 0, 0))
    else:
        for i in range(6, 9):
            cp.pixels[i] = ((25, 0, 0))
        for i in range(1, 4):
            cp.pixels[i] = ((0, 0, 0))