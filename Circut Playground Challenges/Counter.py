from adafruit_circuitplayground import cp

import time
x = 0

while True:
    if cp.button_a:
        cp.pixels[x] = (1, 1, 1)
        time.sleep(.2)
        x = x+  1
   
    if x > 9:
        x = 9
   
    if cp.button_b:
        cp.pixels[x] = (0,0,0)
        time.sleep(.2)
        x = x-1
  
    if x < 0:

        x = 0