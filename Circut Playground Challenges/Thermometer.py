# Every project for this board will need this statement
from adafruit_circuitplayground import cp

# When the program finiches, the baord enters a "waiting" state
# -> flashes all green then off
# We do not want the program to ever end
# That's why we put our work in a while True
# -> runs forever
while True:
    temp_f = cp.temperature
    temp_c = (temp_f * 9 / 5) + 32
   
    
    if temp_c < 78:
        cp.pixels[0] = (0 ,0 ,1)
    if temp_c > 78:
        cp.pixels[1] = (0 ,0 ,1)
    if temp_c > 79:
        cp.pixels[2] = (0 ,0 ,1)
    if temp_c > 80:
        cp.pixels[3] = (1 ,1 ,0)
    if temp_c > 81:
        cp.pixels[4] = (1, 1 ,0)
    if temp_c > 82:
        cp.pixels[5] = (1 ,1 ,0)
    if temp_c > 83:
        cp.pixels[6] = (1 ,1 ,0)
    if temp_c > 84:
        cp.pixels[7] = (1 ,0 ,0)
    if temp_c > 85:
        cp.pixels[8] = (1 ,0 ,0)
    if temp_c > 86:
        cp.pixels[9] = (1 ,0 ,0)