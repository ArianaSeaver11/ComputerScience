from adafruit_circuitplayground import cp

# When the program finiches, the baord enters a "waiting" state
# -> flashes all green then off
# We do not want the program to ever end
# That's why we put our work in a while True
# -> runs forever
import random
import time


while True:
    if cp.button_a:
        cp.pixels.fill((0,0,0))
        roll = random.randint(0,10)
        for i in range(roll):
            cp.pixels[i] = (10, 10, 0)
            time.sleep(0.25)
    if cp.button_b:
        cp.pixels.fill((0,0,0))
