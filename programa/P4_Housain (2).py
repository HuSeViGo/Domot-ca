from microbit import *
import neopixel


np = neopixel.NeoPixel (pin9,1)

while true

     for red in range (0, 255, 5):
         np[0]= (0, red, 0)
         np.show()
         sleep(100)


     for v in range (0, 255, 5):
         np[0]= (v, 0, 0)
         np.show()
         sleep(100)

     for blue in range (0, 255, 5):
         np[0]= (0, 0, blue)
         np.show()
         sleep(100)
