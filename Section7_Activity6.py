from gpiozero import LED, Button
from signal import pause

led_1 = LED(17)
led_2 = LED(27)
led_3 = LED(22)

button = Button(26)

led_1.off()
led_2.off()
led_3.off()

led_index = 0

def switch_led():
    global led_index
    if led_index == 0:
        led_1.on()
        led_2.off()
        led_3.off()
        led_index += 1
    elif led_index == 1:
        led_1.off()
        led_2.on()
        led_3.off()
        led_index += 1
    else:
        led_1.off()
        led_2.off()
        led_3.on()
        led_index = 0

button.when_pressed = switch_led
pause()