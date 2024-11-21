from adafruit_circuitplayground import cp

# When the program finiches, the baord enters a "waiting" state
# -> flashes all green then off
# We do not want the program to ever end
# That's why we put our work in a while True
# -> runs forever
import random
while True:
    a = random.randint(0, 255)
    c = random.randint(0, 255)
    b = random.randint(0, 255)
    x, y, z = cp.acceleration 
    shake_threshold = 9.0
    if abs(x) > shake_threshold:
        cp.pixels[0] = (a,b,a)
        cp.pixels[1] = (a,a,a)
        cp.pixels[2] = (c,b,c)
        cp.pixels[3] = (b,a,b)
        cp.pixels[4] = (b,b,a)
        cp.pixels[5] = (a,a,a)
        cp.pixels[6] = (c,c,c)
        cp.pixels[7] = (b,b,b)
        cp.pixels[8] = (c,a,b)
        cp.pixels[9] = (c,b,c)