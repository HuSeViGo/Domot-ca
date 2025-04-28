from microbit import*

pantalla5 = Image("55555:55555:55555:55555:55555")
esquinas = Image("90009:00000:00900:00000:90009")

while True:
    if button_a.is pressed():
        pin1.write_digital(1)
        display.show("A")
        sleep(2000)
        display.clear()
        display.show(pantalla5)
        sleep(2000)
        display.clear()

    if button_b.is pressed():
        pin1.write_digital(0)
        display.show("B")
        sleep(2000)
        display.clear()
        display.show(esquinas)
        sleep(2000)
        display.clear()

