"""P8 Sensor de luz LDR. Housain Fargoug, 17 de febrero de 2025"""
from microbit import *

led_pin = pin14

while True:
    luz = pin1.read_analog() # leer el pin de lectura del pin1
    display.scroll(str(luz)) # mostrar la matriz de lectura
    if luz < 600: # compreuba el valor de la led
        led_pin.write_digital(1) # enciende el led
    else:
        led_pin.write_digital(0) # apaga el led
        sleep(1000) # Esperar 1 segundo para volver hacer la siguiente acción
