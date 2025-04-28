"""P6 medidor de la temperatura. Housain Fargoug, 11 de febrero de 2025""" 

from microbit import*

while True:

    if button_a.is_pressed():

        temp = temperature
        display.scroll(str(temp) + "C")
        sleep(2000)

    if button_b.is_pressed():
        temp_6 = str (temp - 6)
        display.scroll(temp_6 + "C")
        sleep(2000)
