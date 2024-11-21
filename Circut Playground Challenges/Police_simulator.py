# Every project for this board will need this statement
from adafruit_circuitplayground import cp

# When the program finiches, the baord enters a "waiting" state
# -> flashes all green then off
# We do not want the program to ever end
# That's why we put our work in a while True
# -> runs forever

import time

while True:
    cp.play_tone(500, 0.1)
    cp.pixels.fill((0, 0, 10))
    time.sleep(.5)
    cp.pixels.fill((10, 0, 0))
    time.sleep(.5)
    cp.play_tone(900, 0.1)