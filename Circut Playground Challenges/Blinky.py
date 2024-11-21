# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp

# When the program finiches, the baord enters a "waiting" state
# -> flashes all green then off
# We do not want the program to ever end
# That's why we put our work in a while True
# -> runs forever
import time

while True:

    cp.pixels.fill((0, 0, 0))
    time.sleep(.367)
    cp.pixels.fill((0, 255, 0))
    time.sleep(.367)
